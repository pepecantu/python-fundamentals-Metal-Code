import os
os.system('cls')

names = ["Juan", "María", "Pedro", "Ana"]

unique_names = set(names)

# El operador in se puede usar para verificar si un elemento está en un set

while True:
    name = input("Escribe un nombre (presiona 3 para salir): ")
    if name == "3":
        break
    if name in unique_names:
        print(f"{name} ya está en la lista.")
    else:
        print(f"{name} no está en la lista.")