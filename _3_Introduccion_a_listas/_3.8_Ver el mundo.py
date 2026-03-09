lugares=["Irlanda", "Londres", "Egipto", "Canada", "Alaska"]

print(f"Original: {lugares}")

print(f"Alfabeticamente: {sorted(lugares)}")
print(f"Original: {lugares}")

print(f"Alfabeticamente inverso: {sorted(lugares, reverse=True)}")
print(f"Original: {lugares}")

lugares.reverse()
print(f"Inverso a la anterior: {lugares}")

lugares.reverse()
print(f"inverso a la anterior / Original: {lugares}")

lugares.sort()
print(f"Alfabeticamente: {lugares}")

lugares.sort(reverse=True)
print(f"Alfabeticamente inverso: {lugares}")