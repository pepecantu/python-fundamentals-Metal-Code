import os
os.system("cls")

count = 1

while count <= 10:
    print(count)
    count = count + 1

repeat = True

while repeat:
    print("Hola")
    print("¿Deseas continuar s/n")
    
    res = input()
    
    if res == "n":
        repeat = False
        print("proceso terminado por el usuario")

print("---Numeros nones---")

count2 = 0

while count2 < 10:
    count2 += 1
    
    if count2 % 2 == 0:
        continue
    
    print(count2)
    
print("---Numeros pares---")    
    
count2 = 0

while count2 < 10:
    count2 += 1
    
    if count2 % 2 != 0:
        continue
    
    print(count2)
    
# ("---Parando el ciclo en el num 8---")    
    if count2 == 8:
        break  
