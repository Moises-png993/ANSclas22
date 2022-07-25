import sympy as sp
import numpy as np

a = float(input("ingrese el valor del coeficiente a"))
b = float(input("ingrese el valor del coeficiente b"))
c = float(input("ingrese el valor del coeficiente c"))
datos=[]
p=(3*b-(a**2))/3
q=((2*a**3)-9*a*b+27*c)/27
delta=((q/2)**2)+((p/3)**3)
datos.append(p)
datos.append(q)
datos.append(delta)
if delta==0:
    if p ==0 and q==0:
        x_Uno=(-a/3)
        x_Dos=x_Uno
        x_Tres=x_Dos    
    else: 
        x_Uno=-(3*q)/(2*p) - a/3
        x_Dos=x_Uno
        x_Tres=-(4*p**2)/9*q -(a/3) 
elif delta > 0: 
     
    x_Uno=np.cbrt(-(q/2)+ np.sqrt(delta)) + np.cbrt((-q/2)- np.sqrt(delta)) - (a/3)
    u=np.cbrt(-(q/2)+np.sqrt(delta))
    v=np.cbrt(-(q/2)-np.sqrt(delta))
    datos.append(u)
    datos.append(v)
    x_Dos=-((u+v)/2)-(a/3)+ (sp.sqrt(3))/2*(u-v)*sp.sqrt(-1)
    x_Tres=-((u+v)/2)-(a/3)- (sp.sqrt(3))/2*(u-v)*sp.sqrt(-1)
elif delta < 0:
    teta=np.arccos(-(q/2)/np.sqrt(-(p/3)**3))
    datos.append(teta)
    x_Uno=((2*np.sqrt(-p/3))*(np.cos((teta+2*0*np.pi)/3))-(a/3)) 
    x_Dos=2*np.sqrt(-(p/3))*np.cos((teta+2*1*np.pi)/3)-(a/3)
    x_Tres=2*np.sqrt(-(p/3))*np.cos((teta+2*2*np.pi)/3)-(a/3)

datos = np.array(datos)
np.savetxt("tablaDeIteraciones.csv",datos,delimiter=",")
print(x_Uno)
print(x_Dos)
print(x_Tres)
