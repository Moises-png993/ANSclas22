import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

xi=[0,0,1,1,1]
fi=[-1,-1,0,0,0]
diff=[[-2,10,10,10,],
      [0, 0, 40, 40]]

x = sym.symbols("x")
n = len(xi)
funcion= sym.simplify("x**2*cos(5*x+3)")

#for i in range(0,n):
 #   fi.append(float(funcion.subs(x,xi[i])))

titulo = ['i   ','xi  ','fi  ']

ki = np.arange(0,n,1)
tabla = np.concatenate(([ki],[xi],[fi]),axis=0)
tabla = np.transpose(tabla)


dfinita = np.zeros(shape=(n,n),dtype=float)
tabla = np.concatenate((tabla,dfinita), axis=1)

[n,m] = np.shape(tabla)
diagonal = n-1
j = 3
ordenDiff = 1
while (j < m):

    titulo.append('F['+str(j-2)+']')

    i = 0
    paso = j-2 
    while (i < diagonal):
        denominador = (xi[i+paso]-xi[i])
        numerador = tabla[i+1,j-1]-tabla[i,j-1]
        if numerador==0 and denominador == 0:
            tabla[i,j] = diff[ordenDiff-1][i]/sym.factorial(ordenDiff)
        else:
            tabla[i,j] = numerador/denominador
        i = i+1
    ordenDiff= ordenDiff+1
    diagonal = diagonal - 1
    j = j+1


dDividida = tabla[0,3:]
n = len(dfinita)

x = sym.Symbol('x')
polinomio = fi[0]
for j in range(1,n,1):
    factor = dDividida[j-1]
    termino = 1
    for k in range(0,j,1):
        termino = termino*(x-xi[k])
    polinomio = polinomio + termino*factor

polisimple = polinomio.expand()
tablaPrint=np.array(tabla)
np.savetxt("hermite.csv",tabla,delimiter=",")
print(polisimple)

px = sym.lambdify(x,polisimple)

muestras = 101
a = np.min(xi)
b = np.max(xi)
pxi = np.linspace(a,b,muestras)
pfi = px(pxi)

sustitucion = polisimple.subs(x,0.3926990817)
np.set_printoptions(precision = 4)
print('Tabla Diferencia Dividida')
print([titulo])
print(tabla)
print('dDividida: ')
print(dDividida)
print('polinomio: ')
print(polinomio)
print('polinomio simplificado: ' )
print(polisimple)
print(sustitucion)

plt.plot(xi,fi,'o', label = 'Puntos')
plt.plot(pxi,pfi, label = 'Polinomio')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title('Hermite por diferencias divididas')
plt.show()
