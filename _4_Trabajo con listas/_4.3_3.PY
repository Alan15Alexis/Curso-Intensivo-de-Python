# Uso de range() en Python

# La función range() facilita la generación de secuencias de números.
# Comienza en el primer valor que se le indica y se detiene justo antes del segundo valor.

# Ejemplo: genera los números del 1 al 5
for value in range(1, 6):
    print(value)

# Si se usa un solo argumento, range() comienza desde 0 hasta el número indicado (sin incluirlo)
for value in range(6):  
    print(value)

# Crear una lista a partir de range() usando list()
numeros = list(range(0, 5))  # Genera [0, 1, 2, 3, 4]
print(numeros)

# Usando un tercer argumento en range(), se define un "paso" (intervalo entre valores)
numeros_pares = list(range(2, 10, 2))  # Genera [2, 4, 6, 8]
print(numeros_pares)

# Calcular los cuadrados de los primeros 10 números enteros y almacenarlos en una lista
cuadrados = []
for valor in range(1, 11):
    cuadrado = valor ** 2  # ** es el operador de exponenciación
    cuadrados.append(cuadrado)

print(cuadrados)

# Hacer lo mismo pero de forma más concisa, omitiendo la variable temporal
cuadrados = []
for valor in range(1, 11):
    cuadrados.append(valor ** 2)  # ** exponente

print(cuadrados)

# Funciones útiles para listas numéricas
print(f"Valor mínimo: {min(cuadrados)}")  # Encuentra el valor mínimo
print(f"Valor máximo: {max(cuadrados)}")  # Encuentra el valor máximo
print(f"Suma total: {sum(cuadrados)}")    # Suma todos los valores

# Listas por comprensión: forma más compacta de generar listas
cuadrados = [value ** 2 for value in range(1, 11)]
print(f"Lista por comprensión: {cuadrados}")
