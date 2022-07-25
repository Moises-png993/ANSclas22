import sympy as sp
cifras = -2
Es = 0
while cifras<0:
    cifras = int(input("Ingrese la cantidad de cifras: "))
    if cifras>0:
        Es = 0.5*(10**(2-cifras))
    else:
        print("Ingrese valores positivos, por favor")

valorX=float(input("Ingrese el valor de x: "))
errorAproximado = 1000
aproximacionAnterior = 0
aproximacionActual = 0
i=0
while errorAproximado>Es:
    aproximacionAnterior = aproximacionActual
    aproximacionActual = aproximacionActual+(valorX**i)/float(sp.factorial(i))
    errorAproximado = abs((aproximacionActual-aproximacionAnterior)/aproximacionActual)
    i = i + 1
print(aproximacionActual)