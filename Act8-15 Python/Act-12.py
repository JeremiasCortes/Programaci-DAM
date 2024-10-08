import os

def limpiar():
  os.system('clear')

def Inicio():
  def Conversor_de_Dinero():
    limpiar()
    cantidad_a_convertir = float(input("Introduce la cantidad a convertir: "))
    while True:
      moneda_a_convertir = int(input(
"""
Elije que moneda vas a convertir:
  1. Euro
  2. Dólar

Tu opción: """))
      limpiar()
      match moneda_a_convertir:
        case 1:
          cantidad_a_convertir *= 1.1
          break
        case 2:
          cantidad_a_convertir = f"{cantidad_a_convertir / 1.1:.2f}"
          break
        case _:
          print("Opción no esperada")
          input()
    print(f"Tu conversión es de: {cantidad_a_convertir}")
  limpiar()
  print("Bienvenido al Conversor de € y $")
  while True:
    opcion = int(input(
"""
Que deseas hacer:
  0. Salir
  1. Converitr Dinero

Tu opción es: """))
    match opcion:
      case 0:
        limpiar()
        print("Saliendo...")
        break
      case 1:
        limpiar()
        Conversor_de_Dinero()
        input()
      case _:
        limpiar()
        print("Opción no esperada")
        input()
Inicio()