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
            print(f'[{i}],{aux},{semilla_elevada},{largo_semilla_elevada}, {v}, {r}')
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


def MetodoMultiplicadorConstante(semilla,constante,repeticiones):
    numerosPseudo = []
    if len(str(semilla)) == len(str(constante)) and semilla > 3 and constante > 3:
        for i in range(repeticiones):
            y = semilla * constante
            largo = len(str(y))
            if largo == 8:
                s = str(y)
                t = s[2:6]
                v = int(t)
                r = v / 10000
            else:
                if largo != 8:
                    s = str(y)
                    t = s[1:5]
                    v = int(t)
                    r = v / 10000


            if r in numerosPseudo:
                print("La semilla solo puede generar esta cantidad de numeros PseudoAleatorios: ", len(numerosPseudo))
                break
            else:
                print(f'[{i}],{constante}, {v}, {r}')
                numerosPseudo.append(r)

            semilla = v
        return numerosPseudo


def coprimos(a,b):
    while b != 0:
        a, b = b,a%b

    if a == 1 or a==-1:
        return True
    else:
        return False
def MetodoLineal(semilla,k,g,c,repeticiones):
    numerosPseudo = []
    m = 2**g
    a = 1 + (4*k)
    aux = True
    while aux == True:
        if coprimos(c,m) == True:
            aux = False
        else:
            c = int(input("Ingrese otro valor para C:"))
    for i in range(repeticiones):

        x_i = ((a*semilla)+c)%m
        r = x_i / (m-1)
        if r in numerosPseudo:
            print("La semilla solo puede generar esta cantidad de numeros PseudoAleatorios: ", len(numerosPseudo))
            break
        else:
            print(f'X{i}={a}*{semilla}+{c}mod({m})={x_i} , R{i}={r}' )
            numerosPseudo.append(r)
        semilla = x_i

    return numerosPseudo

MetodoLineal(6,3,3,7,10)




