comidas = ["pizza", "falafel", "carrot cake"]
comida_amigo = comidas[:]  # Copia completa de la lista

comidas.append("cannoli")  # Se agrega un elemento solo a la lista original
comida_amigo.append("helado")  # Se agrega un elemento solo a la copia

print(f"Mi comida favorita es:")
for comida in comidas:
    print(comida)
print(f"La comida favorita de mi amigo es:")
for comida in comida_amigo:
    print(comida)

