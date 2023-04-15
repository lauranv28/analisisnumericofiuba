from math import floor
import numpy as np

#Cantidad de iteraciones a realizar
num = np.array(range(10))
#Creo una lista vacía para guardar los valores calculados en cada iteración
list1 = []
list2 = []

#SECUENCIA 1
for n in num:
    x1 = (-1) ** n
    x2 = (2 * n) + 1
    
    a = 4 * (x1/x2)
    list1.append(a)
    
b = sum(list1)
print(b) 

#SECUENCIA 2
c = 1 / 2
d = 1 / 3

for n in num:
    # Evaluar la sucesion solo para n impar
    if n % 2 == 0:
        continue

    #Determino si el monomio es positivo o negativo
    k = (-1) ** (floor(n/2))

    #Evaluo las constantes
    y1 = (c ** n) / n
    y2 = (d ** n) / n

    z1 = k * y1
    z2 = k * y2
    z3 = 4 * (z1 + z2)
    list2.append(z3)

f = sum(list2)
print(f)

num = range(1, 100, 2)
print(sum(map(lambda n: ((-1)**(floor(n/2)))*((c**n)/n + (d**n)/n), num))*4)
