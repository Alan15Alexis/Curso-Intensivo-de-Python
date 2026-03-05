
#CAMBIAR MAYUSCULAS Y MINUSCULAS
name = "Ada lovelace"
print(name.title()) #Imprime la inicial con mayusculas
print(name.upper()) #Imprime en mayusculas
print(name.lower()) #Imprime con minusculas

#VARIEBLES EN CADENA
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #Cadenas f, formatea la cadena reemplazando el nombre con cualquier variable
message =f"Hello, {full_name.title()}!" #Cadena f con metodo title
print(message)

#AÑADIR ESPACIOS Y TABULACIONES 
print("\nPython") #Salto de linea
print("\tPython") #Tabulacion 
print("Lenguajes\n\tPython\n\tC\n\tJavaScript") #Salto de linea con tabulacion

#Elimiar espacios en blanco
favorite_lenguage = "Python "
print(favorite_lenguage) #Imprime "Python "
print(favorite_lenguage.rstrip()) #Imprime "Python", rstrip limpia espacios a la derecha, lstrip a la izquierda y strip en ambos
