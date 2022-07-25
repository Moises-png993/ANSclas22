import sympy as sp
import numpy as np 

x = sp.symbols('x')
funcion = sp.sympify(input("Ingrese la funcion"))
intervaloUno = int(input("Ingrese el intervalor inferior"))
intervaloDos = int(input("Ingrese el intervalor superior"))
tabla = []
n = 0
if funcion.subs(x,intervaloUno)*funcion.subs(x,intervaloDos) <= 0:
    cifras =-1
    ea=1000
    proximacionAnterior = 0
    xr = 0
    while cifras<0:
        cifras =int(input("Ingrese la cantidad de cifras"))
        if cifras<0:
            print ("No se puede efectuar, introduzca una cifra positiva")
        else:
            es =(0.5*(10**(2-cifras)))


    while ea > es : 
        proximacionAnterior  = xr

        xr = float(intervaloUno - (funcion.subs(x,intervaloUno)*(intervaloUno-intervaloDos))/(funcion.subs(x,intervaloUno)-funcion.subs(x,intervaloDos)))
    
        fx1 = funcion.subs(x,intervaloUno)
        fxr = funcion.subs(x,xr)
        
        cambiaSigno = (fx1)*(fxr)
        
        if cambiaSigno < 0:
            intervaloDos = xr
        if cambiaSigno > 0:
            intervaloUno = xr 
        ea = abs((xr-proximacionAnterior)/xr)*100
        tabla.append([n,intervaloUno,intervaloDos,xr,fx1,fxr,cambiaSigno,ea])
        n = n+1
    tabla=np.array(tabla)
    np.savetxt("tablaIteracion_metFalsaPosicion.csv",tabla,delimiter=",")
else: 
    print("No existe raiz en ese intervalo")