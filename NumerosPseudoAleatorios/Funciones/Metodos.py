def MetodoCuadradosMedios(semilla, repeteciones):
    numerosPseudo = []
    for i in range(repeteciones):
        aux = semilla

        semilla_elevada = aux * aux
        largo_semilla_elevada = len(str(semilla_elevada))

        if largo_semilla_elevada == 8:
            s = str(semilla_elevada)
            t = s[2:6]
            v = int(t)
            r = v / 10000
        else:
            if largo_semilla_elevada != 8:
                s = str(semilla_elevada)
                t = s[1:5]
                v = int(t)
                r = v / 10000

        if r in numerosPseudo:
            print("La semilla solo puede generar esta cantidad de numeros PseudoAleatorios: ",len(numerosPseudo))
            break
        else:
            print(f'[{i}],{aux},{semilla_elevada},{largo_semilla_elevada}', {v}, {r})
            numerosPseudo.append(r)

        semilla = v



        if v == 0:
            print('limite')
            break
        print("fin")

    return numerosPseudo


def MetodoProductosMedios(semilla1,semilla2,repeticiones):
    lista = []
    longitudsemilla1 = len(str(semilla1))

    if(len(str(semilla1)) > 3 and len(str(semilla2)) > 3):
        for i in range(repeticiones):
            multiplicacion = int(semilla1)*int(semilla2)
            aux= str(multiplicacion)
            LongitudNM = len(aux)


            posicionesamostrar = int((LongitudNM - longitudsemilla1) / 2)
            numeroMostrado = aux[posicionesamostrar:posicionesamostrar + int(longitudsemilla1)]

            alista = int(numeroMostrado)
            lista.append((alista/10000))
            semilla1 = semilla2
            semilla2 = alista

        return (lista)
    else:
        print("Porfa digite un numero que contenga mas de 3 numeros")