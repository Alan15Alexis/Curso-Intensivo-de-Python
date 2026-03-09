# Tuplas en Python
# Una tupla es similar a una lista, pero se define con paréntesis en lugar de corchetes.
# La principal diferencia es que una tupla es inmutable, es decir, no se puede modificar después de su creación.

# Definición de una tupla
dimensiones = (200, 20)

# Acceder a los elementos de una tupla usando índices
print(dimensiones[0])
print(dimensiones[1])

# Tuplas con un solo elemento:
# Para definir una tupla con un solo elemento, es obligatorio colocar una coma al final.
tupla_un_elemento = (50,)  # Correcto
no_es_una_tupla = (50)  # Esto es un entero, no una tupla

# Recorrer una tupla con un bucle
print("Dimensiones originales:")
for dimension in dimensiones:
    print(dimension)

# Aunque no se puede modificar una tupla, se puede reasignar completamente con una nueva tupla.
dimensiones = (400, 40)  # Se crea una nueva tupla y se asigna a la misma variable

print("Nueva tupla con dimensiones actualizadas:")
for dimension in dimensiones:
    print(dimension)


# Se deben utilizar tuplas cuando se necesite almacenar un conjunto de valores que no deban modificarse.



