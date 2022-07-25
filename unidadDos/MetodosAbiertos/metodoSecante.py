import numpy as np
import sympy as sp 
cifras = -1 
ea = 1000
x = sp.symbols('x')
xn_menos_uno = float(input("Ingrese el valor de x0"))
xn = float(input("Ingrese el valor de x1"))
funcion = sp.sympify(input("Ingrese la funcion"))
tabla = []
n=0

if funcion.subs(x,xn_menos_uno)*funcion.subs(x,xn) < 0 :

    while cifras < 0:
        cifras = int(input("Ingrese el valor de las cifras"))
        if cifras < 0: 
            print("No se puede calcular")
        else: 
            es=(0.5*10**(2-cifras))
    xn_mas_uno = 0

    while ea >= es: 
        aproximacionAnterior = xn_mas_uno
        xn_mas_uno = float(xn-funcion.subs(x,xn)*((xn-xn_menos_uno)/(funcion.subs(x,xn)-funcion.subs(x,xn_menos_uno)))) 
        xn_menos_uno = xn
        xn = xn_mas_uno
        ea = abs((xn_mas_uno-aproximacionAnterior)/xn_mas_uno)*100
        tabla.append([n,xn_menos_uno,xn,funcion.subs(x,xn_menos_uno),funcion.subs(x,xn),xn_mas_uno,ea])
        n = n+1
    tabla=np.array(tabla)
    np.savetxt("tablaIteracion_metSecante.csv",tabla,delimiter=",")
    print(xn_mas_uno)
else: 
    print("No se puede efectuar dicho problema")
    
        

