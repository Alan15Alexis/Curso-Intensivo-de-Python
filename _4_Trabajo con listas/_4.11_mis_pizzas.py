pizzas = ["peperoni", "hawaiana", "doble queso", "bufalo"]

friend_pizzas = pizzas[:]

pizzas.append("doble queso")
friend_pizzas.append("pollo")

print("Mis pizzas favoritas son:")

for pizza in pizzas:
    print(pizza)

print("Las pizzas fovoritas de mi amigos son:")
for pizza in friend_pizzas:
    print(pizza)