from math import floor
import numpy as np

#Datos de entrada
pi = np.pi
max_iter = np.array(range(100))

def metodo_1(booleano):
    #Precondición
    i = 0
    resultado = 0
    while booleano:
        serie = 4 * (((-1) ** i) / ((2 * i) + 1))
        resultado = resultado + serie
        i += 1
            
        if (resultado == pi) or (i == max_iter.size):
            booleano = False
        else:
            booleano = True
        
        booleano
    return resultado, i

def metodo_2(booleano):
    sum_1 = 0
    sum_2 = 0
    for i in max_iter:
        if i % 2 == 0:
            continue

        signo = (-1) ** (floor(i / 2))
        sum_1 = sum_1 + (signo * ((1/2) ** i) / i)
        sum_2 = sum_2 + (signo * ((1/3) ** i) / i)
        resultado = (sum_1 + sum_2) * 4
        
        i += 1
        booleano
    return resultado, i
    
def aprox_pi():

    #Dato de Entrada
    es_pi = True
    
    aprox_1, iteracion_1 = metodo_1(es_pi)
    aprox_2, iteracion_2 = metodo_2(es_pi)

    #Datos de salida
    print("El número pi (por el método 1) es aproximadamente: ", aprox_1, " en la iteración ", iteracion_1)
    print("El número pi (por el método 2) es aproximadamente: ", aprox_2, " en la iteración ", iteracion_2)

aprox_pi()