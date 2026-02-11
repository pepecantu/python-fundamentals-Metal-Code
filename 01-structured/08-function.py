import os
os.system('cls')

def hi():
    print("Hi")

hi()

def print_add(a, b):
    print(a + b)
    
print_add(3, 4)
    
def add(a, b):
    return a + b

res = add(2, 5)

print(res)

def is_major(age):
    major_age = 18
    
    if age >= major_age:
        return "Si"
    else:
        return "No"

print("Juan tiene 20 años, es mayor de edad?", is_major(20))
print("Ana tiene 15 años, es mayor de edad?", is_major(15))
