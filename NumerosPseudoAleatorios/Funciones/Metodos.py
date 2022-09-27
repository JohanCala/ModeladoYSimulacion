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

def MetodoAditivo(lista, m,n):
    contador=0
    listari =[]
    if ((m) >= 0 and (n) > 0):
        for i in range(0,n+1):

            # sacar primer numero de la lista
            primerelemento = lista[contador]
            # sacar el ultimo elemento de la lista
            ultimo = lista[len(lista)-1]
            # sumatoria de la x final y la x del comienzo
            auxsumatoria= ultimo + primerelemento
            # sacamos el resultado de la nueva semilla con el modulo
            modulo = auxsumatoria % m
            lista.append(modulo)

            ri= (modulo / (m-1))
            listari.append(ri)


            contador+=1

        return listari
    else:
        print("no se pueden ingresar valores inferiores a 0")
        
def MetodoCongruencialCuadratico(a,b,c,m,numerosrecorridas, semilla):
    if(((a % 2) == 0) and ((c % 2) != 0) and ((a % 2) == 0)):
        lista =[]
        for i in range (numerosrecorridas):
            aux = semilla
            # xi+1
            x=((a*semilla**2) + (b* semilla) + c ) % m
            lista.append(x)

            semilla = x
    else:
        print("debe tener encuenta las normas")
    return lista

def MetdoCongruencialMultiplicativo(x0,k,g):
    m = 2 ** g
    a = 5 + (8 * k)
    numerosPseudo = []
    numeroderandom = int(input("Ingrese cuantos numeros pseudoaleatorios desea: "))
    if ((x0) >= 0 and (k) >= 0 and  (g)>=0):
        for i in range(numeroderandom):
            semilla= x0
            #se realiza la parte de a*xi
            aux= a * semilla
            # se realiza el modulo del anterior
            auxmodulo = aux % m
            # el ri
            ri= (auxmodulo / (m-1))
            print(f'X{i}={a}*{semilla}mod({m})={auxmodulo} , R{i}={ri}')
            numerosPseudo.append(ri)
            # cambiamos la semilla
            x0 = auxmodulo
    else:
        print("no se pueden ingresar valores inferiores a 0")


    return numerosPseudo




