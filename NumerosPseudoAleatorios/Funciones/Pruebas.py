import scipy
from scipy.stats import *
import matplotlib.pyplot as plt
from scipy import stats
import math

import math
import statistics
import numpy as np


def PruebaDeMedia(lista):
    valorbuscar= 1-(0.05/2)
    tnormalizacion= scipy.stats.norm.ppf(valorbuscar)
    parteizquierdafinal= 1 / math.sqrt(12* len(lista))
    limiteInferior= (1/2) - ((tnormalizacion)*parteizquierdafinal)
    limiteSuperior= (1/2) + ((tnormalizacion)*parteizquierdafinal)

    print("limite superiror:", limiteSuperior)
    media = statistics.mean(lista)
    print("media de esta secuencia:", media )
    print("limite inferior:", limiteInferior)

    if media <= limiteSuperior and media >= limiteInferior:
        print("la secuencia paso la prueba")
    else:
        print("La secuencia no paso la prueba")


def PruebaDeVarianza(lista):
    alfa = 0.05

    n = len(lista) - 1

    partedeabajolinferior = 12*(n)

    limiteinferiror = (scipy.stats.chi2.ppf(alfa / 2, n)) / partedeabajolinferior

    limitesuperior = (scipy.stats.chi2.ppf(1 - (alfa / 2), n)) / partedeabajolinferior

    varianzaultima = np.var(lista)
    print("limite inferior:", limiteinferiror)
    print("varianza:", varianzaultima)
    print("limite superior:", limitesuperior)

    if (limiteinferiror <= varianzaultima <= limitesuperior):
        print("la secuencia paso la prueba")
    else:
        print("La secuencia no paso la prueba")

def PruebaGrafica(lista):
    fig= plt.figure()
    ax= fig.add_subplot(111)
    res=stats.probplot(lista, dist= stats.norm, sparams=(6,), plot=ax)
    plt.show()

def PruebaDeCorridas(lista):
    a = lista
    listade1o0 = []
    n0 = 0
    n1 = 0
    co = 1

    for i in a:
        if i >= 0.5:
            listade1o0.append(1)
            n1 += 1
        else:
            listade1o0.append(0)
            n0 += 1
    n = n1 + n0
    aux = listade1o0[0]

    for i in range(1, len(listade1o0)):

        if listade1o0[i] != aux:
            co += 1
            aux = listade1o0[i]

    medidaCorridas = ((2 * n1 * n0)) / n + (1 / 2)
    varianzaDeCorridas = ((2 * n1 * n0) * ((2 * n1 * n0) - n)) / ((n ** 2) * (n - 1))
    pruebaEstadistica = (co - medidaCorridas) / (math.sqrt(varianzaDeCorridas))
    intervalo = scipy.stats.norm.ppf(1 - (0.05 / 2))
    print(intervalo)
    print(medidaCorridas)
    print(varianzaDeCorridas)
    print(pruebaEstadistica)

    if pruebaEstadistica >= intervalo * -1 and pruebaEstadistica <= intervalo:
        print("Los datos pasaron la prueba entonce son PseudoAleatorios")
    else:
        print("Los datos no pasaron la prueba")










