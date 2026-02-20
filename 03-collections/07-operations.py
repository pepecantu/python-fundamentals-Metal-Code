import os
os.system('cls')
'''
Cuando hablamos de sets, hablamos de teoría de conjuntos, 
es decir, la unión, la intersección, la diferencia y la diferencia simétrica

'''

# Uniendo dos sets
names1 = {"Juan", "María", "Pedro", "Ana"}
names2 = {"Juan", "Roberto", "Karla", "Ana"}

# se pueden unir con el operador | o con el método union
all_names = names1 | names2
# all_names = names1.union(names2)  # Otra forma de hacerlo

# en los sets las mayúsculas y minúsculas son diferentes, 
# por lo que "Juan" y "juan" serían considerados elementos distintos
print(all_names)

# Intersección de sets, muestra los elementos que están en ambos sets, 
# es decir, los nombres que se repiten en ambos sets
same_names = names1 & names2
# same_names = names1.intersection(names2)  # Otra forma de hacerlo
print(same_names) # muestra los elementos que están en ambos sets

# Diferencia de sets, muestra los elementos que están en el primer set pero no en el segundo
different_names1 = names1 - names2
# different_names = names1.difference(names2)  # Otra forma de hacerlo

print(different_names1) # muestra los elementos que están en uno de los sets pero no en ambos
different_names2 = names2 - names1
print(different_names2) # muestra los elementos que están en uno de los sets pero no

# con el operador ^ o con el método symmetric_difference se pueden obtener 
# los elementos que están en uno de los sets pero no en ambos
different_names = names1 ^ names2
# different_names = names1.symmetric_difference(names2)  # Otra forma de hacerlo
print(different_names) # muestra los elementos que están en uno de los sets pero no en ambos
