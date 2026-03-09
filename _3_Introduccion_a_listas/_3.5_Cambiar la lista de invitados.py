
personas = ["Amlo", "Chavelo", "Homero", "Moreno Valle", 'Mickey Mouse']
invitacion = ['Cordialmente invitada a la persone', 'Invitada a la cena']

print(f"1- {invitacion[0]} {personas[0]}")
print(f"2- {invitacion[1]} {personas[1]}")
print(f"3- {invitacion[0]} {personas[2]}")
print(f"4- {invitacion[1]} {personas[3]}")
print(f"5- {invitacion[0]} {personas[4]}")

print(f" Por cuestiones ajenas a nosotros, no sera posible la presencia de {personas[3]} a nuestro evento")

#Cambiar un valor en una lista
#para suplir el valor de unlista se escribe el nombre de la lista seguido de la posiscion del valor, 
# y se agrtega el nuevo valor
personas[3]= "Mate" #Se esta canbiando el valor del indice 3
print(personas)


print(f"1- {invitacion[0]} {personas[0]}")
print(f"2- {invitacion[1]} {personas[1]}")
print(f"3- {invitacion[0]} {personas[2]}")
print(f"4- {invitacion[1]} {personas[3]}")
print(f"5- {invitacion[0]} {personas[4]}")

#INSERT
#Agrega un nuevo dato en la lista, colocando el 
#numero de indice al que se agregara de la lista consecutivo de el valor

personas.insert(2, "Edge")
print(personas)

#DEL 
#del se utiliza para eliminar un elemnto de una lista, despues de eliminarlo 
#ya no se puede acceder al elemnto eliminado

del personas[0]
print(personas)

#POP
#Aveces necesitamos eliminar un vbalor de una lista y despues necesitarlo, 
# eso hace el metodo pop, elimina o saca el ultimo calor de la lista

popped_personas =personas.pop()#Se almacena en una variable el valor eliminado
print(f"lista completa:\n {personas}")

print(f"valor eliminado: \n {popped_personas}")

#Para eliminar un elemnto y vamos utilizarlo de nuevo, use del, si solo desea retirarlo de la lista, ese pop

#REMOVE
#remueve el valor especifico de una lista
personas.remove("Edge")
print(f"Estos son todos los invitados que asistiran: {personas}")
