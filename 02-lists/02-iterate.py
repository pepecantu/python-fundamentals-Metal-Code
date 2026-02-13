import os
os.system('cls')

names = ["Ana", "Roberto", "Juan"]

# recorrer o iterar una lista
for name in names:
    print(f"Nombre: {name}")

# Recorriendo la lista y agregando (enumerate) para que muestre el (índice) con {index} 
for index, name in enumerate(names):
    print(f"Indice:   {index}- Valor: {name}")
    
# Recorriendo la lista, agregando agregando (enumerate) para que muestre la (posición) con {index + 1}
for index, name in enumerate(names):
    print(f"Posición: {index + 1}- Valor: {name}")
