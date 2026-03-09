

for numero in list(range(1,11)):
    cubo= numero **3
    print(cubo)

cubos= [numero **3 for numero in range(1,11)]
print(f"comprencion de cubos: {cubos}")