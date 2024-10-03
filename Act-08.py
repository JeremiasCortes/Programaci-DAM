import os
os.system('clear')

def SolicitarNumero():
    numberInput = [
        int(input("Introduce el valor de numero 1: ")), 
        int(input("Introduce el valor de numero 2: ")), 
        int(input("Introduce el valor de numero 3: "))
    ]
    os.system('clear')
    print(Suma(numberInput), "\n")
    print(Resta(numberInput), "\n")
    print(Multiplica(numberInput), "\n")
    print(Divide(numberInput), "\n")

def Suma(numbers):
    print("- - - - -    LA SUMA    - - - - -")
    result = f"{numbers[0]} + {numbers[1]} + {numbers[2]} = {numbers[0] + numbers[1] + numbers[2]}"
    return result

def Resta(numbers):
    print("- - - - -    LA RESTA    - - - - -")
    result = f"{numbers[0]} - {numbers[1]} - {numbers[2]} = {numbers[0] - numbers[1] - numbers[2]}"
    return result

def Multiplica(numbers):
    print("- - - - -    LA MULTIPLICACIÓN    - - - - -")
    result = f"{numbers[0]} * {numbers[1]} * {numbers[2]} = {numbers[0] * numbers[1] * numbers[2]}"
    return result

def Divide(numbers):
    print("- - - - -    LA DIVISIÓN    - - - - -")
    result = f"{numbers[0]} / {numbers[1]} / {numbers[2]} = {numbers[0] / numbers[1] / numbers[2]:.2f}"
    return result

SolicitarNumero()