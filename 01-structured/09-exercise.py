import os
os.system('cls')

def print_menu():
    print("Opciones: ")
    print("1. definir tasa de conversión")
    print("2. convertir mondeda")
    print("3. salir")
    print("Elige una opción ")
    res = int(input())
    return res

# Convertir la tasa
def capture_rate():
    print("Ingresa la tasa de conversión del dólar: ")
    rate = float(input())
    return rate

# Convertir a moneda local según la tasa capturada
def convert_currency(rate):
    print("Ingresa la cantidad a convertir: ")
    amount = float(input())
    return amount * rate

option = 0
rate = 0

while option != 3:
    option = print_menu()

    if option == 1:
        rate = capture_rate()
    elif option == 2:
        if rate == 0:
            print("Por favor defina la tasa de conversión primero. ")
            continue
        
        converted_amount = convert_currency(rate)
        print(f"Total en dólares {converted_amount}")
    elif option == 3:
        print("Saliendo del programa...")
    else:
        print("Opción invalida")
