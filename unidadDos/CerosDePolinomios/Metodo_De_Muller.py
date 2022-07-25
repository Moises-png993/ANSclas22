import numpy as np
import sympy as sp

Ea=1000
cifras=-1
x=sp.symbols("x")#simbologia 
x_sub_Cero = float(input("ingrese el primer valor inicial: "))#valores de intervalos iniciales
x_sub_Uno = float(input("ingrese el segundo valor inicial: "))
x_sub_Dos = float(input("ingrese el tercer valor inicial: "))
funcion = sp.sympify(input("Ingrese la funcion: "))#input("ingrese la funcion por favor "))#sympify metodo utilizado para la realizaccion de las matematicas.

#Aqui va el bucle de las cifras
datos_x=[]
datos_y=[]
while cifras < 0:  #1>0
    cifras = (int(input("ingrese la cantidad de cifras significativas:")))
    if cifras < 0:
        print("No se asectan cifras negativas")
    else:
        Es = (0.5*10**(2-cifras))

while Ea > Es: 

    funcion_x_sub_Cero = funcion.subs(x,x_sub_Cero) 
    funcion_x_sub_Uno = funcion.subs(x,x_sub_Uno)
    funcion_x_sub_Dos = funcion.subs(x,x_sub_Dos)#realizacion de funcion para sustitucion de x agregando x_sub_cero etc

    h_sub_Cero = x_sub_Uno - x_sub_Cero
    h_sub_Uno = x_sub_Dos - x_sub_Uno

    ampersand_sub_Cero = ((funcion_x_sub_Uno-funcion_x_sub_Cero)/h_sub_Cero)
    ampersand_sub_Uno = (funcion_x_sub_Dos-funcion_x_sub_Uno)/h_sub_Uno

    
    valor_a = (ampersand_sub_Uno - ampersand_sub_Cero)/(h_sub_Uno + h_sub_Cero)
    valor_b = valor_a*h_sub_Uno + ampersand_sub_Uno
    valor_c = funcion.subs(x,x_sub_Dos)
    discriminante = sp.sqrt(valor_b**2-4*valor_a*valor_c)

    if abs(valor_b + discriminante) > abs(valor_b - discriminante): 

        Xr = x_sub_Dos + (-2*valor_c)/(valor_b + discriminante)
       
    else: 
        Xr = x_sub_Dos + (-2*valor_c)/(valor_b - discriminante)

    Ea=abs((Xr-x_sub_Dos)/Xr)*100
    datos_x.append([x_sub_Cero,x_sub_Uno,x_sub_Dos,funcion_x_sub_Cero,funcion_x_sub_Uno,funcion_x_sub_Dos])
    datos_y.append([h_sub_Cero,h_sub_Uno,ampersand_sub_Cero,ampersand_sub_Uno,valor_a,valor_b,valor_c])
    x_sub_Cero = x_sub_Uno          
    x_sub_Uno = x_sub_Dos
    x_sub_Dos = Xr
datos = np.array(datos_x)
np.savetxt("tablaMuller1.csv",datos,delimiter=",")
datos = np.array(datos_y)
np.savetxt("tablaMuller2.csv",datos,delimiter=",")
    
print(Xr)
print(Ea)