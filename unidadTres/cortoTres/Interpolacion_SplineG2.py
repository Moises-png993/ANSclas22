import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
def trazaCuadratica(xs,ys):
    x = sp.symbols("x")
    n = len(xs)
    k = 0 
    ecu1=[]
    ecu1y=[]
    for i in range (2,n):
        ecu11=[]
        a=(xs[i-1])**2
        b=(xs[i-1])
        c=1
        d=(ys[i-1])
        p=(3*(n-1))-3
        for i in range (p):
            ecu11.append(0)
        if a ==((xs[1]**2)):
            a = 0
        ecu11.insert(k,c)
        ecu11.insert(k,b)
        ecu11.insert(k,a)
        ecu1.append(ecu11)
        ecu1y.append(d)
        k=k+3
    k=3
    ecu2=[]
    ecu2y=[]
    for i in range (2,n):
        ecu22=[]
        a=(xs[i-1])**2
        b=(xs[i-1])
        c=1
        d=(ys[i-1])
        p=(3*(n-1))-3
        for i in range(p):
            ecu22.append(0)
        ecu22.insert(k,c)
        ecu22.insert(k,b)
        ecu22.insert(k,a)
        ecu2.append(ecu22)
        ecu2y.append(d)
        k=k+3

    ecu3=[0,xs[0],1]
    p=(3*(n-1))-3
    for i in range (p):
        ecu3.append(0)
    ecu3y=ys[0]
    a=(xs[n-1])**2
    ecu4=[a,xs[n-1],1]
    p=(3*(n-1))-3
    for i in range(p):
        ecu4.insert(0,0)
    ecu4y=ys[n-1]
    w=3
    u=0
    ecu5=[]
    ecu5y=[]
    for i in range(2,n):
        ecu55 = []
        p = (3*(n-1))-4
        for k in range(p):
            ecu55.append(0)
        a = (xs[i-1])*2
        b = 1
        ecu55.insert(u,b)
        if a == (xs[1])*2:
            a1=0
            ecu55.insert(u,a1)
        else:
            ecu55.insert(u,a)
        ecu55.insert(w,-b)#aca
        ecu55.insert(w,-a)
        ecu5.append(ecu55)
        u = u + 3
        w =w + 3
        ecu5y.append(0)
    ecu6 = [1]
    p = (3*(n-1))-1
    for k in range(p):
        ecu6.append(0)
    ecu6y = 0
    matriz = []
    matrizy = []
    for i in range(len(ecu1)):
        matriz.append(ecu1[i])
        matrizy.append(ecu1y[i])
        matriz.append(ecu2[i])
        matrizy.append(ecu2y[i])

    matriz.append(ecu3)
    matrizy.append(ecu3y)

    matriz.append(ecu4)
    matrizy.append(ecu4y)

    for i in range(len(ecu5)):
        matriz.append(ecu5[i])
        matrizy.append(ecu5y[i])

    matriz.append(ecu6)
    matrizy.append(ecu6y)
    tabla=np.array(matriz)
    np.savetxt("matriz.csv",tabla,delimiter=",")
    tabla=np.array(matrizy)
    np.savetxt("matrizy.csv",tabla,delimiter=",")
    #for line in matriz:
     #  print('  '.join(map(str, line)))
    coeficientes = np.linalg.solve(matriz,matrizy)
    count = 0
    px_tabla = []
    for i in range (0,n-1):
        pxtramo=coeficientes[count]*x**2+coeficientes[count+1]*x+coeficientes[count+2]
        count = count+3
        px_tabla.append(pxtramo)
    return px_tabla
xi = [1,2,3,4] 
fi = [4,8,12,16]
n=len(xi)
muestras=10
px_tabla=trazaCuadratica(xi,fi)    
print('Polinomios por tramos: ')
for tramo in range(1,n,1):
    print(' x = ['+str(xi[tramo-1])
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

plt.plot(xi,fi,'ro', label='puntos')
plt.plot(xtraza,ytraza, label='trazador'
         , color='blue')
plt.title('Trazadores Cúbicos Naturales')
plt.xlabel('xi')
plt.ylabel('px(xi)')
plt.legend()
plt.show()