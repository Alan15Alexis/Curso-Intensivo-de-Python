
# ==========================================
# TEMA: Cadenas y Variables en Python
# ==========================================

# 1. CREAR Y NOMBRAR VARIABLES (Naming Variables)
# En Python, asignamos un valor a una variable usando el signo '='.
# Buena práctica: Usar nombres descriptivos y en minúsculas.
# Aquí, 'nombre' es nuestra etiqueta y "Fredy" es el valor en memoria.
nombre = "Fredy"

# Creamos una segunda variable descriptiva llamada 'pregunta'.
# Almacenamos una cadena de texto (String) identificada por las comillas dobles.
pregunta = "¿Te gustaría aprender Python?"

# 2. USAR VARIABLES Y F-STRINGS 
# Utilizamos la función print() para mostrar el resultado en la consola.
# La letra 'f' antes de las comillas activa la interpolación de cadenas.
# Las llaves {} le dicen a Python: "Ejecuta lo que hay aquí dentro y pon su valor en el texto".
print(f"¡Buen día {nombre}! {pregunta}")