
# =====================================================================
# TEMA: Modificar mayúsculas y minúsculas en Cadenas 
# =====================================================================

# Tenemos una variable con un nombre escrito de forma irregular 
# (algunas mayúsculas, otras minúsculas).
nombre = "Fredy manuel Perez hernandez"

# Imprimimos el valor original. 
# Python respeta exactamente cómo fue escrito.
print("Original:")
print(nombre) 

# 1. Método title(): Formato de Título
# Ideal para mostrar nombres propios o títulos de artículos.
# Pone la primera letra de cada palabra en mayúscula.
print("\nFormato Título (title):")
print(nombre.title()) # Salida: Fredy Manuel Perez Hernandez

# 2. Método upper(): Todo a Mayúsculas
# Útil si queremos enfatizar un texto o simular que estamos "gritando".
print("\nTodo Mayúsculas (upper):")
print(nombre.upper()) # Salida: FREDY MANUEL PEREZ HERNANDEZ

# 3. Método lower(): Todo a Minúsculas
# Súper útil en bases de datos para guardar información de forma estándar,
# evitando que "Fredy" y "fredy" se registren como dos personas distintas.
print("\nTodo Minúsculas (lower):")
print(nombre.lower()) # Salida: fredy manuel perez hernandez