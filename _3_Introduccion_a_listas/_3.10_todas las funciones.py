peliculas = ["El Padrino",
    "El Caballero de la Noche",
    "Pulp Fiction",
    "Forrest Gump",
    "Matrix",
    "Titanic",
    "Inception",
    "Gladiador",
    "La Lista de Schindler",
    "Parásitos"]

print(peliculas)
#Acceder a la lista
print(peliculas[5])
print(peliculas[4].title())

#Modificar elementos de una lista
peliculas[0]="Sonic"
print(peliculas)

#Añadir elementos al final de una lista
peliculas.append("Tito")
print(peliculas)

#Añadir elementos en un indice especifico de una lista
peliculas.insert(0, "100 años")
print(peliculas)

#Eliminar elemnetos de una lista
del peliculas[0]
print(peliculas)

#Remover un elemento de una lista
pelicula_eliminada=peliculas.pop(0)
print(f"pelicula eliminada: {pelicula_eliminada}")

#Eliminar un elemento por valor
peliculas.remove("Tito")
print(peliculas)