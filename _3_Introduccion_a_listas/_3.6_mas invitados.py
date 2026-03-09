personas = ["Amlo", "Chavelo", "Homero", "Moreno Valle", 'Mickey Mouse']
invitacion = ['Cordialmente invitada a la persone', 'Invitada a la cena']

print(f"1- {invitacion[0]} {personas[0]}")
print(f"2- {invitacion[1]} {personas[1]}")
print(f"3- {invitacion[0]} {personas[2]}")
print(f"4- {invitacion[1]} {personas[3]}")
print(f"5- {invitacion[0]} {personas[4]}")
print ("Se ha expandido el cupo de invitados a la reunion, A continuacion se presenta la lista actualizada:")

personas.insert(2, "Maria de todos los angeles")
personas.insert(3, "Triple H")
personas.append("EPN")
print(personas)

print(f"1: {invitacion[0]} {personas[6]}")
print(f"2: {invitacion[1]} {personas[1]}")
print(F"3: {invitacion[0]} {personas[3]}")
print(f"4: {invitacion[1]} {personas[5]}")
print(f"5: {invitacion[0]} {personas[2]}")
print(f"6: {invitacion[1]} {personas[0]}")
print(f"7: {invitacion[1]} {personas[7]}")
print(f"8: {invitacion[0]} {personas[4]}")
