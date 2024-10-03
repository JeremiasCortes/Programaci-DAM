import os

def SolicitarNumeros():
    inputnumbers = {"base": int(input("Introduce el número 1: ")), "exponente": int(input("Introduce el numero 2: "))}
    os.system("clear")
    print(Potencia(inputnumbers))

def Potencia(num):
    resultado = num["base"] ** num["exponente"]
    return resultado

SolicitarNumeros()