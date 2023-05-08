def son_igual_signo(a, b):
    return a * b >= 0


def biseccion(f, a, b, epsilon, iteraciones_restantes):
    medio = (a + b) / 2
    f_a = f(a)
    f_b = f(b)
    f_medio = f(medio)

    if iteraciones_restantes <= 0:
        print("Se excedieron las iteraciones maximas")
        return None
    if son_igual_signo(f_a, f_b):
        print("No se puede determinar raices con biseccion ya que f(a) y f(b) tienen igual signo")
        return None

    if abs(f_a) <= epsilon:
        return a
    if abs(f_b) <= epsilon:
        return b
    if abs(f_medio) <= epsilon:
        return medio

    if son_igual_signo(f_b, f_medio):
        return biseccion(f, a, medio, epsilon, iteraciones_restantes-1)

    return biseccion(f, medio, b, epsilon, iteraciones_restantes-1)


def ejemplo():
    print('Metodo de biseccion')
    print('f(x) = x^4 -5x^3 + 25')

    f = lambda x: (x ** 4) - 5 * (x ** 3) + 25
    epsilon = 0.001
    max_iteraciones = 100
    a = 1
    b = 3
    raiz = biseccion(f, a, b, epsilon, max_iteraciones)

    if raiz:
        print("Raiz encontrada: {0:.3f} +- {1:.3f}".format(raiz, epsilon))


if __name__ == '__main__':
    ejemplo()

