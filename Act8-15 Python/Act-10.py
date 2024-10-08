import os

def SolicitarNumeros():
    inputnumbers = {"base": int(input("Introduce el número 1: ")), "divisor": int(input("Introduce el numero 2: "))}
    os.system("clear")
    print(Resto(inputnumbers))

def Resto(num):
    resultado = num["base"] % num["divisor"]
    return resultado

SolicitarNumeros()