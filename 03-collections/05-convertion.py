import os
os.system('cls')

# Conversión de una tupla a una lista
my_tuple = (1,2,3,4,5)

my_list = list(my_tuple) # haciendo la conversión

print(my_list)
print(type(my_list))

my_list.append(6) # agregando un item a la lista

print(my_list)  
print(type(my_list))
print(my_tuple)
print(type(my_tuple))


# Convertir una lista a una tupla
names = ["Ana", "Pedro", "Francisco", "Naomi"]
print(names)
print(type(names))

names_tuple = tuple(names)
print(names_tuple)
print(type(names_tuple))
