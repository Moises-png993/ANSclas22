import math
import numpy as np

cifras = -1
ea = 1000
tabla = []
c = 0
while cifras < 0:
    cifras = int(input("Ingrese la cantidad de cifras"))
    if cifras < 0:
        print("No se puede efectuar")
    else:
        es = 0.5*(10**(2-cifras))

valorDeX = float(input("Introduzca el valor de x"))
resultado = 1+valorDeX
n = 2
contador = 0

while ea > es:
    aproxAnterior = resultado
    resultado = resultado + (valorDeX**n)/math.factorial(n)
    ea = abs((resultado-aproxAnterior)/resultado)*100
    n = n+1
    contador = contador + 1
    tabla.append([c,resultado,ea])
    c +=1

tabla=np.array(tabla)
np.savetxt("tablaIteraciones_ex.csv",tabla,delimiter=",")
    
print("El valor es ", resultado)
print("El error es ", ea)
print("El numero de iteraciones",contador)