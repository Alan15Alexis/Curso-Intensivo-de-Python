# Bucle FOR en Python

# Un bucle `for` permite recorrer secuencias (listas, tuplas, cadenas, etc.)
# y ejecutar un bloque de código para cada elemento de la secuencia.

reyes = ["Melchor", "Gaspar", "Baltazar"]

# Recorrer una lista e imprimir cada elemento

# 🔹 Explicación:
# - `for`: Palabra clave que indica el inicio del bucle.
# - `variable`: Nombre de la variable que tomará el valor de cada elemento en la iteración.
# - `in`: Palabra clave que indica que se recorrerá un iterable.
# - `iterable`: Objeto que se recorrerá (lista, tupla, string, `range()`, etc.).
# - `Bloque de código`: Código indentado que se ejecuta en cada iteración.


for rey in reyes:
    print(rey)

# Usar un bucle `for` con una estructura más elaborada
for rey in reyes:
    print(f"{rey.title()} ha realizado un truco increíble.")
    print(f"Estamos emocionados de que nos muestres tu siguiente truco, {rey.title()}.\n")

# Mensaje final después del bucle (fuera del bloque `for`)
print("¡Excelente show, muchas gracias por su participación!")
