import os
os.system('cls')

# Dividir y asignar a variables una tupla

data = ("Juan", 30, "México")

name, age, country = data # Asignación multiple de cada uno de los items de la tupla a una variable

print(name)
print(age)
print(country)

print("--------------")

# Operador unpacked (*)
# Asignando sólo ciertos items [0][1] a variables one,two (unpacking)
# y el resto a una variable con *last_numers se envía a una lista [3,4,5]

numbers = (1,2,3,4,5)

one, two, *last_numbers = numbers

print(one)
print(two)
print(last_numbers)

print("--------------")

# Asignando los primeros items a una lista con la variable *first_numbers [1,2,3] y el resto
# y el resto se asigna a una variable en forma individual (unpacking)
print("--------------")

*first_numbers, four, five = numbers
print(first_numbers)
print(four)
print(five)

# Asignando el primer y último elemento a una variable first y fifth (unpacking)
# y los elementos de enmedio se van a una lista con el *middle [3,4,5]
print("--------------")

first, *middle, fifth = numbers

print(first)
print(middle)
print(fifth)

# Unpacking con un string
print("--------------")

name = "Jacinto"

j,a, *the_rest = name

print(j)
print(a)
print(the_rest)
