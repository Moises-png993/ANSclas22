#Metodo Abiertos Ecuaciones Cuadraticas 

import sympy as sp
x=sp.symbols("x")
polinomio = sp.sympify(input("ingrese el polinomio"))# metodo sympify simplifica la expresion matematica 
raices=sp.solve(polinomio,x)
print(raices)