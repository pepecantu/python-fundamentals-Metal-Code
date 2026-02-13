import os
os.system('cls')

numbers = [5, 2, 9, 1, 5, 6]

# Ordenar la lista en forma invertida
numbers.reverse()
print(numbers)

# Ordenar la lista en forma ascendente
numbers.sort()
print(numbers)

# Ordenar en forma descendente
numbers.sort(reverse = True)
print(numbers)

# Volver a ordenar ascendente
numbers.sort()
print(numbers)
