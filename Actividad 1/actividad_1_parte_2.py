import numpy as np

def mejor_aproximacion(numero1, numero2):
    """Calcula cuál es el número con menor error"""
    diferencia = []
    aprox = 0
    resta = numero2 - numero1
    if resta > 0:
        diferencia.append(resta)
        menor = diferencia[0]
        if resta < menor:
            aprox = resta
    return aprox


def metodo_1(booleano):
    pi = np.pi
    resultado = 0
    n = 0
    while booleano == False:
        serie = 4 * (((-1) ** n) / ((2 * n) + 1))
        resultado = resultado + serie
        """ 
        Esta parte como está propuesta no funciona porque la primer iteración ya es menor que pi
        entonces va a recorrer el while 1 vez y me va a quedar es_pi = True y termina la ejecución

        if resultado < pi:
            booleano = True
        else:
            n += 1 """

        booleano
    return resultado, n

def main():
    #Condición inicial para ambos métodos
    es_pi = False
    
    print(metodo_1(es_pi))

main()