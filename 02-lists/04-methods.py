import os
os.system('cls')

data = ["Pedro", "Ana", "Joaquín", "María", "Jesús"]

print(data)

# Agregar otro elemento al final
data.append("Luis")
print(data)

# Agregar elemento en un índice específico [0] = posición (1)
data.insert(0, "Jesús")
print(data)

# Agregar elemento en el índice [2] = posición (3)
data.insert(2, "Lucía")
print(data)

# Eliminar el primer elemento repetido
data.remove("Jesús")

# Eliminar el primer elemento por el índice
#data.pop(0) # elimina a Pedro
#print(data)

# Muestra el elemento eliminado con .pop
name = data.pop(0) # muestra a Pedro
print(name)

print(data)  # muestra como esta la lista en este momento después de eliminar a Pedro

# Editar
# supliendo a "Lucía" índice [0] por "Sofía" 
data[0] = "Sofía"
print(data)
