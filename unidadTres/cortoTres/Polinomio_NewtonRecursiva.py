import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols("x")
xi = [2,5,7]
fi = [4,25,49]
b  = []
puntos = len(xi)
numerador=1
"""
funcion = sp.sympify("E**x")
for i in range(0,puntos):
    fi.append(float(funcion.subs(x,xi[i])))
"""
b.append(fi[0])
b.append((fi[1]-b[0])/(xi[1]-xi[0]))

for  i in range(2,puntos):
    temp = (((fi[i]-fi[i-1])/(xi[i]-xi[i-1]))-b[i-1])/(xi[i]-xi[0])
    b.append(temp)
    """
    if(i==puntos-1 and puntos>3):
        temp=(b[i]-b[i-1])/(xi[i]-xi[0])
        b[i]=temp
    """
    
print(b)
polinomio = b[0]
for i in range(0,puntos-1):
    numerador = numerador*(x-xi[i])
    polinomio = polinomio + b[i+1]*numerador



polisimple = polinomio.expand()
print(polisimple)

px = sp.lambdify(x,polisimple)
muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)

plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Recursiva - Newton')
plt.show()