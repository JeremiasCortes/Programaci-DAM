import os

def limpiar():
  os.system('clear')

def Inicio():
  limpiar()

  while True:
    valor = int(input(
"""
Bienvenido al conversor de días!!

Elije una opción:
  0. Salir
  1. Horas
  2. Minutos
  3. Segundos

Opción que escoges: """
    ))
    limpiar()
    dias = int(input("Introduce la cantidad de días a convertir: "))
    match valor:
      case 0:
        print("Saliendo...")
        break
      case 1:
        print(f"{dias} en horas son: {valor*24}")
        input()
        limpiar()
      case 2:
        print(f"{dias} en minutos son: {valor*24*60}")
        input()
        limpiar()
      case 3:
        print(f"{dias} en segundos son: {valor*24*60*60}")
        input()
        limpiar()
      case _:
        print("Opción no válida. Por favor, elige de nuevo.")
        input()
        limpiar()
Inicio()