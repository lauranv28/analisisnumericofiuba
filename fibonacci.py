#import numpy as np

#Condiciones iniciales
x1 = 1
x2 = 1

#Secuencia de números
#seq = np.array(range(50))

#Serie de Fibonacci
print("SECUENCIA DE FIBONACCI")
for i in range(50):
    x = x2 + x1
    print("Número", i, ":",x)
    #Actualizo los nuevos valores
    x1 = x2
    x2 = x

