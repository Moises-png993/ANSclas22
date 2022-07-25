import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def trazalineal(xi,fi):
    n = len(xi)
    x = sp.Symbol('x')
    px_tabla = []
    tramo = 1
    while not(tramo>=n):
        numerador = fi[tramo]-fi[tramo-1]
        denominador = xi[tramo]-xi[tramo-1]
        m = numerador/denominador
        pxtramo = fi[tramo-1] + m*(x-xi[tramo-1])
        px_tabla.append(pxtramo)
        tramo = tramo + 1     
    return(px_tabla)

xi = [1,2,3,4] 
fi = [4,8,12,16]
muestras = 10 
n = len(xi)
px_tabla = trazalineal(xi,fi)
print('Polinomios por tramos: ')

for tramo in range(1,n,1):
    print('  x = ['+str(xi[tramo-1])
          +','+str(xi[tramo])+']')
    print(str(px_tabla[tramo-1]))
xtraza = np.array([])
ytraza = np.array([])
tramo = 1

while not(tramo>=n):
    a = xi[tramo-1]
    b = xi[tramo]
    xtramo = np.linspace(a,b,muestras)
    pxtramo = px_tabla[tramo-1]
    pxt = sp.lambdify('x',pxtramo)
    ytramo = pxt(xtramo)
    xtraza = np.concatenate((xtraza,xtramo))
    ytraza = np.concatenate((ytraza,ytramo))
    tramo = tramo + 1

plt.plot(xi,fi,'o', label='puntos')
plt.plot(xtraza,ytraza, label='trazador')
plt.title('Trazadores lineales (splines)')
plt.xlabel('xi')
plt.ylabel('px(xi)')
plt.legend()
plt.show()