#Organizar una lista

#Sort
#Ordena alfabeticamente el orden de la lista
#Nota: Toma primero los valores que tienen mayuscula

coches = ["audi", "volkswagen", "Porche", "BYD", "OLINIA", "Tesla"]
coches.sort()
print(coches)

#reverse=True
#Ordenar alfabeticamente inverso
#Nota: El cambio de valores es permanente en ambos casos
coches.sort(reverse=True)
print(coches)

#Sorted
#Metodo para cambiar el orden a-z, z-a, temporal
autos = ["audi", "volkswagen", "Porche", "BYD", "OLINIA", "Tesla"]

print("Esta es la lista original:")
print(autos)

print("Esta es la lista modificada")
print(sorted(autos))

print("Esta es la lista original de nuevo")
print(autos)

#Reverse
#Imprimir lista en inverso, temporal
#Solo invirte los valores de una la lista, no los modifica en orden alfabetico a-z o z-a
autos.reverse()
print(f"La lista de autos inversa: \n {autos}")

autos.reverse()
print(f"La lista de autos original: \n {autos}")

#Len()
#Muestra la longitud de una lista

len(autos)
print(len(autos))