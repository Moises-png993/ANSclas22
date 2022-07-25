import numpy as np
import sympy as sp
cifras=-1
Ea=1000
xUno=float(input("ingrese el valor inicial:"))
x=sp.symbols("x")
funcion=sp.sympify(input("ingrese la funcion f(x) a derivar:"))
funcionOne=funcion.diff(x)
funcionTwo=funcionOne.diff(x)
tabla=[]

if abs(funcion.subs(x,xUno)*funcionTwo.subs(x,xUno)/(funcionOne.subs(x,xUno)**2))<1:
    
    while cifras<0:
        cifras=int(input("ingrese la cantidad de cifras significativas:"))
        if cifras>0:
          Es=(0.5*(10**(2-cifras)))  #error de tolerancia Es
        else:
          print("por favor no ingrese cifras negativas")
    
    while Ea>Es:#1000>0.05 true
        xn=xUno
        xUno=xn-((funcion.subs(x,xn)*funcionOne.subs(x,xn))/(funcionOne.subs(x,xn)**2-(funcion.subs(x,xn)*funcionTwo.subs(x,xn))))
        Ea=abs((xUno-xn)/xUno)*100
        print(xUno)
        tabla.append([xn,funcion.subs(x,xn),funcionOne.subs(x,xn),xUno,Ea])
    
    tabla=np.array(tabla)
    np.savetxt("newtonRapson.csv",tabla,delimiter=",")
      
else:
  print("No existe convergencia")
        