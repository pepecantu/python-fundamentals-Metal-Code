import os
os.system('cls')

people = {
    'name': 'Karla',
    'age': 30,
    'country': 'Mexico',
    'hobbies': ['leer', 'viajar', 'correr'],
    'address': {                            # Diccionario anidado
        'street': 'Calle Falsa 123',
        'city': 'CDMX',
        'zip_code': '12345'
    }   
}

print(people['name'])
print(people['age'])
print(people['country'])
print(people['hobbies'])

# Acceder a una clave del diccionario
people['name'] = 'Carlos'
print(people['name'])

# Eliminar una clave y su valor del diccionario
del people['age']
print(people)

for key in people:
    print(f"Clave: {key}")
    
for value in people.values():
    print(f"Valor: {value}")

for key, value in people.items():
    print(f"Clave: {key}, Valor: {value}")
    
print(people['address'])
