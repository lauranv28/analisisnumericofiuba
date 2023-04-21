import numpy as np

#Le pongo un valor límete a las iteraciones porque sino me queda loop infinito
#Precondición: max_iteraciones > 0
max_iteraciones = np.array(range(1000000))

def metodo_1(booleano):
    pi = np.pi
    resultado = 0
    while booleano:
        for n in max_iteraciones:
            serie = 4 * (((-1) ** n) / ((2 * n) + 1))
            resultado = resultado + serie
        
            """  Esta parte como está propuesta no funciona porque la segunda iteración ya es menor que pi
            entonces va a recorrer el while 2 veces, queda es_pi = True y termina la ejecución"""

            if resultado == pi:
                booleano = False
            else:
                booleano = True

        booleano
    #Pongo para que devuelva también el valor de la aproximación
    return resultado, n 

def main():
    #Precondición para ambos métodos: 
    es_pi = True
    
    #Devuelve el número calculado y la iteración en la que se alcanzó
    numero, iteracion = metodo_1(es_pi)
    #Devuelve el número con menor error
    print("El número pi es aproximadamente: ", numero, " en la iteración ", iteracion)

main()