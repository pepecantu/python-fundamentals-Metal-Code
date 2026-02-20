import os
os.system('cls')

# funciones que regresan una tupla

def get_stadistics(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = 0
    if count > 0:
        average = total / count
    return total, count, average

numbers = (1,2,3,4,5)    
tuple_result = get_stadistics(numbers)

print(tuple_result)
print(type(tuple_result))
