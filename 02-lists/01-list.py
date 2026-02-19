import os
os.system('cls')

numbers = [1,2,3,4,5]

print(numbers)

# Imprimiendo el primer número (1) que esta en el índice [0]
print(numbers [0])

# Imprimiendo el último número (5) que esta en el índice (4)
print(numbers [4])

# Imprimiendo el último número (5) que esta en el índice (4) pero utilizando el signo de (-) que inicia a partir del el último índice
print(numbers [-1])

# Función creada para insertar mensaje para separar la impresión en pantalla
def show (list):
    print("Imprimiendo la lista modificada")
    print(list)
    
# Modificando los valores que existen en la lista, cambiamos el valor del íncide [0] del (1) por un (10)
numbers[0] = 10
show(numbers) # Show se utiliza para llamar a la función del mensaje que separa la impresión de pantalla

# Utilizano la mutabilidad de las listas 
# modificamos el índice [1]= numero (2)  por ('Juan') y el índice [2]= numero (3) por (3.14) que son diferentes tipos de datos
numbers [1] = 'Juan'
numbers [2] = 3.14

show(numbers)

# Utilizando el dinamismo de la lista (se utiliza el . después del nombre de la variable (numbers.append()) para obtener métodos
numbers.append("Agregamos algo más") # Se agrega a la lista el string del mensaje

show(numbers)

# Se agrega también una lista como parámetro dentro de la lista para agregar múltiples elementos a la lista.
numbers.extend([6,7,8])

show(numbers)
