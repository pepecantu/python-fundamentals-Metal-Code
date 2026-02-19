import os
os.system('cls')

'''
los set o conjuntos para evitar elementos duplicados, estas colecciones ordenan los elementos
creando un hash interno para que sea mucho más rápido obtener la información de los elementos
El set se utiliza para ver si un elemento existe o no existe en una colección de información y
es más rápido que una tupla o una lista
'''
numbers = { 1, 1,2, 3,4,5,5,1,2,3}
print(numbers)

# al agregar items si estos items estan duplicados no se agregarán
numbers.add(6)  # Se agrega
numbers.add(1)  # No se agrega por estar repetido
numbers.add(2)  # No se agrega por estar repetido

print(numbers)

# Eliminación de items
numbers.remove(3)
print(numbers)

# también se puede recorrer
for number in numbers:
    print(f"Número: {number}")

# En las listas se repiten los items
print("Lista con elementos repetidos")
my_list = [1,6,7,2,3,4,5,1,2,3]
print(my_list)

# Convirtiendo la lista en set para elminar los items repetidos
print("Lista convertida a set elimina items repetidos y los ordena")
my_set = set(my_list)
print(my_set)
