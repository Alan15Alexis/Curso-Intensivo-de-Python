#!/usr/bin/env python3
"""
Music Lyrics Sync
Reproduce música con la letra sincronizada al estilo de Apple Music.
Soporta URLs de YouTube y Apple Music.

Uso:
  python main.py
  python main.py https://www.youtube.com/watch?v=...
  python main.py https://music.apple.com/...

Controles durante la reproducción:
  ESPACIO   — Pausar / Reanudar
  ← →       — Retroceder / Adelantar 10 segundos
  ESC / Q   — Salir
"""

import sys
import os
import re
import time
import tempfile
import shutil
from dataclasses import dataclass
from typing import Optional

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------

def _ensure_deps():
    pkgs = {
        "pygame": "pygame",
        "yt_dlp": "yt-dlp",
        "syncedlyrics": "syncedlyrics",
        "requests": "requests",
        "bs4": "beautifulsoup4",
    }
    missing = [pip for mod, pip in pkgs.items() if not _importable(mod)]
    if missing:
        print(f"Instalando: {' '.join(missing)}")
        os.system(f"{sys.executable} -m pip install {' '.join(missing)} -q")


def _importable(name: str) -> bool:
    try:
        __import__(name)
        return True
    except ImportError:
        return False


_ensure_deps()

import pygame          # noqa: E402  (after install check)
import yt_dlp          # noqa: E402
import syncedlyrics    # noqa: E402
import requests        # noqa: E402
from bs4 import BeautifulSoup  # noqa: E402


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class SongInfo:
    title: str
    artist: str
    duration: float = 0.0


@dataclass
class LyricLine:
    timestamp: float   # seconds from start
    text: str


# ---------------------------------------------------------------------------
# URL handler — extracts song info from YouTube / Apple Music
# ---------------------------------------------------------------------------

class URLHandler:

    @staticmethod
    def detect_source(url: str) -> str:
        if re.search(r"(youtube\.com/watch|youtu\.be/)", url):
            return "youtube"
        if "music.apple.com" in url:
            return "apple_music"
        raise ValueError("Solo se aceptan URLs de YouTube o Apple Music.")

    @staticmethod
    def get_youtube_info(url: str) -> SongInfo:
        with yt_dlp.YoutubeDL({"quiet": True, "no_warnings": True}) as ydl:
            info = ydl.extract_info(url, download=False)

        title = info.get("track") or info.get("title", "Desconocido")
        artist = info.get("artist") or info.get("uploader", "Desconocido")

        for suffix in (" - Topic", "VEVO", " Official", " Music"):
            artist = artist.replace(suffix, "").strip()

        return SongInfo(title=title, artist=artist, duration=info.get("duration", 0))

    @staticmethod
    def get_apple_music_info(url: str) -> SongInfo:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
        }
        resp = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(resp.content, "html.parser")

        og_title = soup.find("meta", property="og:title")
        raw = og_title.get("content", "") if og_title else ""

        # Apple Music format: "Song Name - Single - Artist" or "Song Name - Artist"
        parts = [p.strip() for p in raw.split(" - ") if p.strip()]
        title = parts[0] if parts else raw
        artist = parts[-1] if len(parts) > 1 else ""

        # Filter out common non-artist fragments
        if artist.lower() in {"single", "ep", "album", ""}:
            artist = parts[-2] if len(parts) > 2 else ""

        return SongInfo(title=title, artist=artist)


# ---------------------------------------------------------------------------
# Audio handler — downloads audio via yt-dlp
# ---------------------------------------------------------------------------

class AudioHandler:

    def __init__(self, work_dir: str):
        self.work_dir = work_dir

    def download_youtube(self, url: str) -> str:
        return self._download(url)

    def search_and_download(self, query: str) -> str:
        print(f"  Buscando en YouTube: «{query}»")
        return self._download(f"ytsearch1:{query}")

    def _download(self, source: str) -> str:
        template = os.path.join(self.work_dir, "audio.%(ext)s")

        opts_with_ffmpeg = {
            "format": "bestaudio/best",
            "outtmpl": template,
            "noplaylist": True,
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
        opts_no_ffmpeg = {
            "format": "bestaudio/best",
            "outtmpl": template,
            "noplaylist": True,
        }

        try:
            with yt_dlp.YoutubeDL(opts_with_ffmpeg) as ydl:
                ydl.download([source])
        except Exception:
            with yt_dlp.YoutubeDL(opts_no_ffmpeg) as ydl:
                ydl.download([source])

        for ext in ("mp3", "m4a", "ogg", "opus", "webm", "wav"):
            path = os.path.join(self.work_dir, f"audio.{ext}")
            if os.path.exists(path):
                return path

        for f in os.listdir(self.work_dir):
            if f.startswith("audio."):
                return os.path.join(self.work_dir, f)

        raise FileNotFoundError("No se pudo encontrar el archivo de audio descargado.")


# ---------------------------------------------------------------------------
# Lyrics handler — fetches & parses LRC-format synced lyrics
# ---------------------------------------------------------------------------

class LyricsHandler:

    @staticmethod
    def fetch(artist: str, title: str) -> list:
        """Return a sorted list of LyricLine objects, or empty list."""
        searches = [
            f"{title} {artist}",
            title,
        ]
        for q in searches:
            try:
                lrc = syncedlyrics.search(q, allow_plain_format=False)
                if lrc:
                    lines = LyricsHandler._parse_lrc(lrc)
                    if lines:
                        return lines
            except Exception:
                pass

        # Direct LRCLib API call as fallback
        try:
            return LyricsHandler._fetch_lrclib(artist, title)
        except Exception:
            pass

        return []

    @staticmethod
    def _fetch_lrclib(artist: str, title: str) -> list:
        resp = requests.get(
            "https://lrclib.net/api/search",
            params={"artist_name": artist, "track_name": title},
            timeout=10,
        )
        resp.raise_for_status()
        for item in resp.json():
            if item.get("syncedLyrics"):
                return LyricsHandler._parse_lrc(item["syncedLyrics"])
        return []

    @staticmethod
    def _parse_lrc(lrc: str) -> list:
        pattern = re.compile(r"\[(\d{1,2}):(\d{2})\.(\d{2,3})\](.*)")
        lines = []
        for raw in lrc.splitlines():
            m = pattern.match(raw.strip())
            if not m:
                continue
            mins, secs = int(m.group(1)), int(m.group(2))
            frac_str = m.group(3)
            frac = int(frac_str) / (1000 if len(frac_str) == 3 else 100)
            text = m.group(4).strip()
            if text:
                lines.append(LyricLine(timestamp=mins * 60 + secs + frac, text=text))
        return sorted(lines, key=lambda l: l.timestamp)


# ---------------------------------------------------------------------------
# Karaoke display — pygame-based, smooth-scroll, Apple Music style
# ---------------------------------------------------------------------------

class KaraokeDisplay:

    WIDTH = 820
    HEIGHT = 700
    FPS = 60
    HEADER_H = 72
    BG = (22, 22, 25)
    SLOT_H = 68          # Fixed slot height for each lyric row
    LERP_SPEED = 0.12    # Smoothing factor (0 = no movement, 1 = instant)

    # (max abs-distance, font_size, rgb_color, alpha)
    STYLE = [
        (0.6,  52, (255, 255, 255), 255),   # current line
        (1.6,  34, (180, 180, 185), 210),   # ±1
        (2.6,  26, (120, 120, 125), 170),   # ±2
        (3.6,  20, ( 80,  80,  85), 130),   # ±3
        (5.0,  16, ( 55,  55,  60), 90),    # ±4
    ]

    def __init__(self):
        pygame.init()
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Music Lyrics Sync")
        self.clock = pygame.time.Clock()

        self._fonts: dict[int, pygame.font.Font] = {}
        self._base_font = self._find_system_font()

        # Pre-render gradient overlays (created once, blitted every frame)
        self._top_fade = self._make_gradient(self.WIDTH, 110, self.BG, 220, 0)
        self._bot_fade = self._make_gradient(self.WIDTH, 110, self.BG, 0, 220)

        self.song: Optional[SongInfo] = None
        self.lyrics: list = []
        self.smooth_idx: float = 0.0
        self.paused = False

    # ── Font helpers ────────────────────────────────────────────────────────

    def _find_system_font(self) -> Optional[str]:
        for name in ("dejavusans", "ubuntucondensed", "ubuntu", "freesansbold",
                     "liberationsans", "notosans", "arial"):
            path = pygame.font.match_font(name)
            if path:
                return path
        return None

    def font(self, size: int) -> pygame.font.Font:
        if size not in self._fonts:
            self._fonts[size] = (
                pygame.font.Font(self._base_font, size)
                if self._base_font
                else pygame.font.Font(None, size)
            )
        return self._fonts[size]

    # ── Gradient helper ─────────────────────────────────────────────────────

    @staticmethod
    def _make_gradient(w: int, h: int, color: tuple,
                       alpha_start: int, alpha_end: int) -> pygame.Surface:
        surf = pygame.Surface((w, h), pygame.SRCALPHA)
        for y in range(h):
            a = int(alpha_start + (alpha_end - alpha_start) * y / h)
            pygame.draw.line(surf, (*color, a), (0, y), (w, y))
        return surf

    # ── Style lookup ────────────────────────────────────────────────────────

    def _style_for(self, distance: float):
        """Return (font_size, color, alpha) based on float distance from current line."""
        abs_d = abs(distance)
        for max_d, size, color, alpha in self.STYLE:
            if abs_d < max_d:
                return size, color, alpha
        return 14, (40, 40, 45), 60

    # ── Audio helpers ────────────────────────────────────────────────────────

    def _elapsed(self) -> float:
        return max(0.0, pygame.mixer.music.get_pos() / 1000.0)

    def _current_int_idx(self, elapsed: float) -> int:
        idx = 0
        for i, line in enumerate(self.lyrics):
            if line.timestamp <= elapsed:
                idx = i
        return idx

    def _toggle_pause(self):
        if self.paused:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        self.paused = not self.paused

    def _seek(self, delta: float):
        pos = max(0.0, self._elapsed() + delta)
        try:
            pygame.mixer.music.set_pos(pos)
        except Exception:
            pass

    # ── Drawing ──────────────────────────────────────────────────────────────

    def _draw_lyrics(self, smooth_idx: float):
        if not self.lyrics:
            f = self.font(26)
            msg = f.render("No se encontró letra sincronizada", True, (100, 100, 110))
            self.screen.blit(msg, ((self.WIDTH - msg.get_width()) // 2, self.HEIGHT // 2))
            return

        center_y = (self.HEADER_H + self.HEIGHT) // 2
        pad_left = 42
        max_w = self.WIDTH - pad_left - 30

        for i, line in enumerate(self.lyrics):
            distance = i - smooth_idx
            # Skip lines that are too far away to be visible
            if abs(distance) > 5.5:
                continue

            size, color, alpha = self._style_for(distance)
            f = self.font(size)

            text = line.text
            # Truncate if wider than display area
            while f.size(text)[0] > max_w and len(text) > 6:
                text = text[:-2] + "…"

            surf = f.render(text, True, color)
            surf.set_alpha(alpha)

            y = center_y + distance * self.SLOT_H - surf.get_height() // 2
            self.screen.blit(surf, (pad_left, int(y)))

    def _draw_header(self, elapsed: float):
        # Background strip
        hdr = pygame.Surface((self.WIDTH, self.HEADER_H), pygame.SRCALPHA)
        hdr.fill((14, 14, 17, 230))
        self.screen.blit(hdr, (0, 0))
        pygame.draw.line(self.screen, (55, 55, 62),
                         (0, self.HEADER_H - 1), (self.WIDTH, self.HEADER_H - 1))

        if not self.song:
            return

        pad = 22
        title_surf = self.font(21).render(self.song.title, True, (235, 235, 240))
        artist_surf = self.font(15).render(self.song.artist, True, (140, 140, 152))
        self.screen.blit(title_surf, (pad, 13))
        self.screen.blit(artist_surf, (pad, 38))

        mins, secs = divmod(int(elapsed), 60)
        label = f"{mins:02d}:{secs:02d}" + ("  ⏸" if self.paused else "")
        t_surf = self.font(18).render(label, True, (140, 140, 152))
        self.screen.blit(t_surf, (self.WIDTH - t_surf.get_width() - pad, 26))

    def _draw_hint(self):
        f = self.font(13)
        hint = "ESPACIO: Pausa  |  ← →: ±10 s  |  ESC / Q: Salir"
        s = f.render(hint, True, (65, 65, 72))
        self.screen.blit(s, ((self.WIDTH - s.get_width()) // 2, self.HEIGHT - 22))

    # ── Main loop ────────────────────────────────────────────────────────────

    def run(self, song: SongInfo, lyrics: list, audio_path: str):
        self.song = song
        self.lyrics = lyrics

        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        hint_until = time.time() + 6

        while True:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_ESCAPE, pygame.K_q):
                        pygame.quit()
                        return
                    if event.key == pygame.K_SPACE:
                        self._toggle_pause()
                    if event.key == pygame.K_LEFT:
                        self._seek(-10)
                    if event.key == pygame.K_RIGHT:
                        self._seek(10)

            # Music finished?
            if not pygame.mixer.music.get_busy() and not self.paused:
                time.sleep(1)
                pygame.quit()
                return

            elapsed = self._elapsed()
            target_idx = self._current_int_idx(elapsed)

            # Smooth-lerp toward the target index
            self.smooth_idx += (target_idx - self.smooth_idx) * self.LERP_SPEED

            # Draw
            self.screen.fill(self.BG)
            self._draw_lyrics(self.smooth_idx)

            # Fade overlays (top and bottom)
            self.screen.blit(self._top_fade, (0, self.HEADER_H))
            self.screen.blit(self._bot_fade, (0, self.HEIGHT - 110))

            self._draw_header(elapsed)
            if time.time() < hint_until:
                self._draw_hint()

            pygame.display.flip()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

BANNER = """
╔══════════════════════════════════════╗
║        Music Lyrics Sync            ║
║  Letra sincronizada con la música   ║
╚══════════════════════════════════════╝
"""


def main():
    print(BANNER)

    url = (sys.argv[1].strip() if len(sys.argv) > 1
           else input("Pega la URL (YouTube o Apple Music):\n  > ").strip())

    if not url:
        sys.exit("Error: no se proporcionó URL.")

    try:
        source = URLHandler.detect_source(url)
    except ValueError as e:
        sys.exit(f"Error: {e}")

    print(f"\n[1/4] Fuente: {source.replace('_', ' ').title()}")

    work_dir = tempfile.mkdtemp(prefix="music_sync_")

    try:
        # --- Song info ---
        print("[2/4] Obteniendo información de la canción...")
        if source == "youtube":
            info = URLHandler.get_youtube_info(url)
        else:
            info = URLHandler.get_apple_music_info(url)

        print(f"  Título:  {info.title}")
        print(f"  Artista: {info.artist}")

        # --- Download audio ---
        print("[3/4] Descargando audio...")
        audio = AudioHandler(work_dir)
        if source == "youtube":
            audio_path = audio.download_youtube(url)
        else:
            query = f"{info.artist} {info.title} audio oficial"
            audio_path = audio.search_and_download(query)
        print(f"  Listo: {os.path.basename(audio_path)}")

        # --- Fetch lyrics ---
        print("[4/4] Buscando letra sincronizada...")
        # Strip featured artists for a cleaner search
        artist_clean = re.split(r"\s*(feat\.?|ft\.?|&|,)\s*", info.artist,
                                flags=re.IGNORECASE)[0].strip()
        lyrics = LyricsHandler.fetch(artist_clean, info.title)

        if lyrics:
            print(f"  ✓ {len(lyrics)} líneas encontradas")
        else:
            print("  ⚠ No se encontró letra — la canción se reproducirá sin letra")

        # --- Launch ---
        print("\nAbriendo reproductor... (ESC / Q para salir)\n")
        KaraokeDisplay().run(info, lyrics, audio_path)

    except KeyboardInterrupt:
        print("\nInterrumpido.")
    except Exception as e:
        import traceback
        print(f"\nError: {e}")
        traceback.print_exc()
        sys.exit(1)
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)

    print("¡Hasta la próxima! 🎵")


if __name__ == "__main__":
    main()
