import sys


from Funciones.Metodos import *
from Funciones.Pruebas import *


try:
    semilla = int(input("Ingrese la Semilla"))
    if semilla >= 1000 and semilla <= 9999:
        repeticiones = int(input("ingrese las repeticiones a generar"))
        nums = MetodoCuadradosMedios(semilla,repeticiones)
    else:
        print("Ingrese numero de 4 digitos")

    PruebaGrafica(nums)



except (ValueError):
    print("Error tipo: ", sys.exc_info()[0])
    print("digite valores correctos")