import os
os.system("cls")

number1 = 15
number2 = 5.5

result = number1 + number2

print(result)
print(type(result))

result2 = "Hola " + str(number1)
print(result2)
print(type(result2))

number_str = "20"
number_cast = int(number_str)

print(number_cast)
print(type(number_cast))

decimal_str = "3.14"
decimal_cast = float(decimal_str)

print(decimal_cast)
print(type(decimal_cast))

decimal_lost = int(3.99)
print(decimal_lost)
print(type(decimal_lost))

age = 25
name = "Pedro"
print(name + " tiene " + str(age))
