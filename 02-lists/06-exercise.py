import os
os.system('cls')

names = []

def print_menu():
    print("Menu ")
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Ver lista")
    print("4. Salir")

def add(list):
    item = input("Ingrese el nombre a agregar: ")
    list.append(item)
    list.sort()
    print(f"{item} ha sido agregado a la lista")

def remove(list):
    item = input("Ingrese el nombre a eliminar: ") 
    if item in list:
        list.remove(item)
        list.sort()
        print(f"{item} ha sido eliminado de la lista")
    else:
        print(f"{item} no se encuentra en la lista")

def show(list):
    if len(list) == 0:
        print("La lista esta vacía")
    else:
        print("Los nombres son:")
        for item in list:
            print(f"- {item}")
            
while True:
    print_menu()
    option = input("Selecciones una opción: ")
    
    if option == '1':
        add(names)
    elif option == '2':
        remove(names)
    elif option == '3':
        show(names)
    elif option == '4':
        print("Saliendo del programa")
        break
    else:
        print("Opción no válida")
