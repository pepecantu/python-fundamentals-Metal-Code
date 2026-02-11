import os
os.system("cls")

age = 65

if age >= 18 and age < 60:
    print("Eres mayor de edad")
elif age >=13 and age < 18:
    print("Eres un adolecente")
elif age >= 60:
    print("Eres un adulto mayor")
else:
    print("Eres menor")
