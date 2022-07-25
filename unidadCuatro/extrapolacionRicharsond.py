import sympy as sp 
from diferenciacionNumerica import DiferenciaNumerica

x = sp.symbols("x")
h = float(input("Ingrese el valor de H: "))
funcion = sp.sympify(input("Ingrese la funcion: "))
valor = float(input("Ingrese el valor de x: "))
nivel = int(input("Ingrese el nivel de Richarsond: "))

hs = []
f= []
D = []
hs.append(h)
for i in range(0,nivel):
    hs.append(hs[i]/(2))

print(hs)

for i in range(0,nivel):
    resultado = DiferenciaNumerica(valor,hs[i],funcion)
    f.append(resultado.divCentral())

print(f)

#Nivel 2
for i in range(0,nivel-1):
    D.append((4/3)*f[i+1]-(1/3)*f[i])

D3 = []
#Nivel 3
for i in range(0,nivel-2):
   D3.append((16/15)*D[i+1]-(1/15)*D[i])



#Nivel 4
D4 = []
for i in range(0,nivel-3):
    D4.append((64/63)*D3[i+1]-(1/63)*D3[i])
print(D4)
"""
D5=(256/255)*D4[1]-(1/255)*D4[0]

print(D5)
"""