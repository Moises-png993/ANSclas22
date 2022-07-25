import sympy as sp #importaciones de librerias 
import numpy as np
cifras=-1
Ea=1000
x=sp.symbols("x")
funcion=sp.sympify("2*x-4*sin(x)")#metodo sympify nos ayuda a las funciones matematicas
funcionDerivada=funcion.diff(x)#metodo usado para derivar 
xUno=sp.sympify(float(input("ingrese el valor inicial")))
#evaluando convergencia
tabla=[]
if abs(funcionDerivada.subs(x,xUno))<1:
    while cifras<0:  #1>0
       cifras=(int(input("ingrese la cantidad de cifras significativas")))
    if cifras<0:
        print("No se asectan cifras negativas")
    else:
        Es=(0.5*10**(2-cifras))
    
        
    while Ea > Es:
        
        xn=xUno
        xUno=float(funcion.subs(x,xUno))
        Ea=abs((xUno-xn)/xUno)*100
        tabla.append([float(xn),float(xUno),float(Ea)])
  
    tabla=np.array(tabla)
    np.savetxt("puntoFijo.csv",tabla,delimiter=",")
else:
    print("no existe convergencia")


