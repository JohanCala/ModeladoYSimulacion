from math import log
import math
import numpy as np
from math import e
import matplotlib.pyplot as plt


forma= 5
escala = 0.3

def visual_basic(semilla, cantidad):
    ri = []

    m = math.pow(2, 24)
    xi = semilla
    for i in range(0, cantidad):
        temp = int((1140671485 * (xi) + 12820163) % m)
        r = temp / (m - 1)
        ri.append(r)
        xi = temp

    return ri


def fortran(semilla, cantidad):
    ri = []

    xi = semilla
    for i in range(0, cantidad):
        r = int(630360016 * (xi) % (math.pow(2, 31) - 1))
        temp = r / ((math.pow(2, 31) - 1) - 1)

        xi = r

        ri.append(temp)

    return ri




def ziboxmullersen(lista2, lista1):
    listaaux = []
    for i in range(0, len(lista2)):
        zi= (math.sqrt(-2 * log(lista2[i], 10))) * math.sin(2 * math.pi * lista1[i])
        listaaux.append(zi)
    return listaaux

def ziboxmullercos(lista2, lista1):
    listaaux = []
    for i in range(0, len(lista2)):
        zi= (math.sqrt(-2 * log(lista1[i], 10))) * math.cos(2 * math.pi * lista2[i])
        listaaux.append(zi)
    return listaaux




#print("ditribucion de logaritmo natural")
def distribucionlognormal(ziboxmullersen1):
    listaaux = []
    for i in range(0, len(ziboxmullersen1)):
        formula= e ** ziboxmullersen1[i]
        listaaux.append(formula)

    return listaaux


def distribucionchicuadrado(ziboxmullersen1, ziboxmullersen2, ziboxmullersen3):
    listaaux = []
    suma= []
    for i in range(0, len(ziboxmullersen1)):
        lista1cuadrado= ziboxmullersen1[i]**2
        lista2cuadrado=ziboxmullersen2[i]**2
        lista3cuadrado = ziboxmullersen3[i]**2
        sumaaux= lista1cuadrado + lista2cuadrado + lista3cuadrado
        suma.append(sumaaux)

    return suma

def distribuciont(ziboxmullersen1, ziboxmullersen2, ziboxmullersen3):
    
    operacion = []
    for i in range(0,len(ziboxmullersen1)):
        fraccionario = ((ziboxmullersen2[i]*2 + ziboxmullersen3[i] + [i]*2 / 3))
        raiz = math.sqrt(fraccionario)
        operacioncompleta = ziboxmullersen1[1] / raiz
        operacion.append(operacioncompleta)
    
    return operacion
                        

            


def distribucionF(ziboxmullersen1, ziboxmullersen2):
    division = []
    for i in range(0, len(ziboxmullersen1)):
        formula= ziboxmullersen1[i] **2 / ziboxmullersen2[i] **2
        division.append(formula)

    return division




def distribucionexponencial(ziboxmullersen1):
    listaformulacompleta= []
    while True:
        try:
            tasa = int(input("Escribe tu tasa: "))
        except ValueError:
            print("Debes escribir un número.")
            continue

        if tasa <= 0:
            print("Debes escribir un número positivo.")
            continue
        else:
            break
    for i in range(0, len(ziboxmullersen1)):
        formulaparte1= -1/tasa
        formulaparte2 = log(ziboxmullersen1[i], 10)
        formulatotal = formulaparte1 * formulaparte2
        listaformulacompleta.append(formulatotal)
    return listaformulacompleta





def distribuciongamma(r1,r2):
    #parte 1
    a = 1 / math.sqrt((2*forma)-1)

    b = forma - math.log10(4)

    q= forma + (1/forma)

    teta = 4.5
    d = 1 + math.log10(teta)
    #parte 3
    vif = []
    zif = []
    yif = []
    wif = []
    for i in range(0 , len(r1)):

        vi = a * math.log10((r1[i]/(1-r2[i])))

        vif.append(vi)


        zi = (r1[i]**2) * r2[i]
        zif.append(zi)




    for j in range(0,len(vif)):
        yi = forma * math.e ** vif[j]
        yif.append(yi)


        wi = b + q * vif[j]-yi
        wif.append(wi)


    #parte 4
    dGF = []

    for k in range(0, len(vif)):
        if wif[k] + d -(teta*zif[k]) > 0 :
            dGi = escala * yif[k]

            dGF.append(dGi)


        else:
            if wif[k] >= math.log10(zif[k]):
                dGi = escala * yif[k]
                dGF.append(dGi)


            else:
                print("el conjunto de numeros pseudo aletorios no cumple con la condicion vuelve a sacar otro conjunto ")

    return dGF

""" 
lista1= fortran(255, 1000)

lista2= fortran(257, 1000)
print(distribuciongamma(lista1,lista2))
plt.hist(distribuciongamma(lista1,lista2),80)
plt.show()
"""