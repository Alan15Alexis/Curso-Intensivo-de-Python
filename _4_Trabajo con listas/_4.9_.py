# Partir una lista (Slice)
# Un "slice" es una técnica que permite trabajar con un grupo específico de elementos dentro de una lista.
# Para definir un slice, se indica el índice inicial y el índice final (pero el último índice NO se incluye).

jugadores = ["Carlos", "Martina", "Michael", "Flor", "Eli"]

# Seleccionar los primeros tres elementos (índices 0, 1 y 2)
print(jugadores[0:3])  

# Omisión de índices en slices:
# - Si se omite el primer índice, Python asume que el slice inicia desde el principio de la lista.
# - Si se omite el segundo índice, Python asume que el slice termina al final de la lista.

print(f"Desde el primer elemento: {jugadores[:4]}")  # Desde el inicio hasta el índice 3
print(f"Hasta el último jugador: {jugadores[2:]}")   # Desde el índice 2 hasta el final
print(f"Los últimos 3 jugadores: {jugadores[-3:]}")  # Últimos 3 elementos de la lista

# Uso de slices en un bucle
print("Aquí están los tres primeros jugadores de mi equipo:")
for jugador in jugadores[:3]:  # Iterar sobre los primeros tres elementos
    print(jugador.title())

# Copiar una lista usando slices
# [:] permite hacer una copia de la lista original sin afectar la original
comidas = ["pizza", "falafel", "carrot cake"]
comida_amigo = comidas[:]  # Copia completa de la lista

print(f"Mi comida favorita es: {comidas}")
print(f"La comida favorita de mi amigo es: {comida_amigo}")

comidas.append("cannoli")
comida_amigo.append("helado")

print(f"Mi comida favorita es: {comidas}")
print(f"La comida favorita de mi amigo es: {comida_amigo}")
