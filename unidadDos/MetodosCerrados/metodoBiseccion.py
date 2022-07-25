import numpy as np
import sympy as sp

x = sp.symbols('x')
funcion = sp.sympify(input("ingrese la funcion:"))

intervaloUno = int(input("Ingrese el intervalor inferior"))
intervaloDos = int(input("Ingrese el intervalor superior"))
n = 0
tabla = []

if funcion.subs(x,intervaloUno)*funcion.subs(x,intervaloDos) < 0:
    cifras =-1
    ea=1000
    proximacionAnterior = 0
    xr = 0
    numIteracion = 0
    #tabla = [] #Se declara matriz
    while cifras<0:
        cifras =int(input("Ingrese la cantidad de cifras"))
        if cifras<0:
            print ("No se puede efectuar, introduzca una cifra positiva")
        else:
            es =(0.5*(10**(2-cifras)))
    

    while ea > es : 
         
        proximacionAnterior  = xr
        xr = (intervaloUno+intervaloDos)/2
        fx1 = funcion.subs(x,intervaloUno)
        fxr = funcion.subs(x,xr)
        cambiaSigno = (fx1)*(fxr)
        tabla.append([intervaloUno,intervaloDos,xr,fx1,fxr,cambiaSigno,ea])
        if cambiaSigno < 0:
            intervaloDos = xr
        if cambiaSigno > 0:
            intervaloUno = xr 
    
        ea = abs((xr-proximacionAnterior)/xr)*100
        n = n+1
    tabla = np.array(tabla)
    np.savetxt("tablaDeIteraciones.csv",tabla,delimiter=",")
else: 
    print("No existe raiz en ese intervalo")
print("La raiz es",xr)