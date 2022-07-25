import sympy as sp
from Tartaglia import *


A= float(input("ingrese el coeficiente de a")) 
B= float(input("ingrese el coheficiente de b")) 
C= float(input("ingrese el coheficiente de c")) 
D= float(input("ingrese el coeficiente de d")) 
datos=[]
    #one step:calcula 
 
P=(8*B-3*A**2)/8 
Q=(8*C-4*A*B+A**3)/8 
R=(256*D-64*A*C+16*A**2*B-3*A**4)/256 
datos.append(P)
datos.append(Q)
datos.append(R)
a=-P/2 
b=-R 
c=((4*P*R)-(Q**2))/8
 #three step: Sustitucion de U en una de la ecuaciones y resolucion de v y w
resultado_cubica = tartaglia(a,b,c)
u=resultado_cubica.resultado()
v=sp.sqrt((2*u)-P)
w=-Q/(2*v)   
r=u**2-w**2
 #four step: Encontrar las raicezsc  s
datos.append(v)
datos.append(w)
datos.append(r)
x_uno = (v+sp.sqrt(v**2-4*(u-w)))/2-A/4
x_dos = (v-sp.sqrt(v**2-4*(u-w)))/2-A/4
x_cuatro = (-v-sp.sqrt(v**2-4*(u+w)))/2-A/4
x_tres = (-v+sp.sqrt(v**2-4*(u+w)))/2-A/4
datos = np.array(datos)
np.savetxt("tablaDeIteraciones.csv",datos,delimiter=",")
print(x_uno)
print(x_dos)
print(x_tres)
print(x_cuatro)