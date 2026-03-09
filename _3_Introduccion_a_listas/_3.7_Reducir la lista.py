personas = ["Amlo", "Chavelo", "Homero", "Moreno Valle", 'Mickey Mouse',"Maria de todos los angeles", "Triple H", "EPN"]
invitacion = ['Cordialmente invitada a la persone', 'Invitada a la cena']


print(f"1: {invitacion[0]} {personas[6]}")
print(f"2: {invitacion[1]} {personas[1]}")
print(F"3: {invitacion[0]} {personas[3]}")
print(f"4: {invitacion[1]} {personas[5]}")
print(f"5: {invitacion[0]} {personas[2]}")
print(f"6: {invitacion[1]} {personas[0]}")
print(f"7: {invitacion[1]} {personas[7]}")
print(f"8: {invitacion[0]} {personas[4]}")

print("Nota: Se le recuerda que solo debe de ingresar como maximo de dos acompañantes.")

primer_eliminado = personas.pop(3)
segundo_eliminado = personas.pop(1)
tercer_eliminado = personas.pop(5)
cuarto_eliminado = personas.pop (0)
quinto_eliminado = personas.pop(3)

print(f"Jugador {primer_eliminado} eliminado")
print(f"Jugador {segundo_eliminado} eliminado")
print(f"Jugador {tercer_eliminado} eliminado")
print(f"Jugador {cuarto_eliminado} eliminado")
print(f"Jugador {quinto_eliminado} eliminado")
print(personas)
print(f"¡Felicitaciones! jugadores {personas[0]} y {personas[1]}, seran acredores de una lujosa cena.")

del personas[0]
del personas[1]
del personas[0]

print(personas)