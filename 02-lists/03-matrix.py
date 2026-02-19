import os
os.system('cls')

# Lista bi-dimensional ó una lista dentro de otra lista
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# Accediendo lista matrix índice [0] = [1,2,3] y a el índice [0] de la lista que esta en el índice de matrix [0] es el (1)
# En la matrix tenemos las listas [0] = [1,2,3] la lista [1] = [4,5,6] y la lista [2] = [7,8,9,]
# Y en cada lista [1,2,3] el índice [0] = 1 en la lista [4,5,6] el índice [0] = 4 y en la lista [7,8,9] el índice [0] = 7 
print(matrix[0][0]) # envía el 1
print(matrix[1][0]) # envía el 4
print(matrix[2][0]) # envía el 7

# Recorriendo las 3 listas que contiene la lista matrix
def show(m):
    print("Matriz:")
    for row in m:   # Recorre la lista matriz
        for element in row: # Recorre cada una de las listas
            print(element)
show(matrix)

# Agregando otra lista en el índice [3] de la lista matrix
matrix.append([10,11,12])
show(matrix)

# Se agrega también listas múltiples dentro de la lista matrix
matrix.extend([
    [13,14,15],
    [16,17,18]
])

show(matrix)