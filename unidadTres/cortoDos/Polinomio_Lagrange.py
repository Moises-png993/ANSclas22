import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


xi = []
fi = []
x = sym.symbols("x")
funcion= sym.simplify("E**x")
puntos = int(input("Ingrese los puntos a interpolar: "))

for i in range(0,puntos):
    xi.append(float(input(f"Ingrese el valor de x{i}: ")))
    fi.append(float(funcion.subs(x,xi[i])))

print(xi)
print(fi)

n = len(xi)
x = sym.Symbol('x')
polinomio = 0
divisorL = np.zeros(n, dtype = float)
for i in range(0,n,1):

    numerador = 1
    denominador = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerador = numerador*(x-xi[j])
            denominador = denominador*(xi[i]-xi[j])
    terminoLi = numerador/denominador

    polinomio = polinomio + terminoLi*fi[i]
    divisorL[i] = denominador


polisimple = polinomio.expand()
sustitucion = polisimple.subs(x,0.25)

px = sym.lambdify(x,polisimple)


muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)


print('    valores de fi: ',fi)
print('divisores en L(i): ',divisorL)
print()
print('Polinomio de Lagrange, expresiones')
print(polinomio)
print()
print('Polinomio de Lagrange: ')
print(polisimple)
print(sustitucion)

plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Interpolación Lagrange')
plt.show()