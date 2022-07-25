import sympy as sp
#Dado tres puntos se pueden obtener una relacion cuadratica
x = sp.symbols("x")
x_sub_0 = float(input("Ingrese el valor de Xo: "))
y_sub_0 = float(input("Ingrese el valor de f(Xo): "))
x_sub_1 = float(input("Ingrese el valor de x1: "))
y_sub_1 = float(input("Ingrese el valor de f(x1): "))
x_sub_2 = float(input("Ingrese el valor de X3: "))
y_sub_2 = float(input("Ingrese el valor de f(x3): "))

b0 = y_sub_0
b1 = (y_sub_1-y_sub_0)/(x_sub_1-x_sub_0)
b2 = ((y_sub_2-y_sub_1)/(x_sub_2-x_sub_1)-(y_sub_1-y_sub_0)/(x_sub_1-x_sub_0))/(x_sub_2-x_sub_0)
print(b0,b1,b2)

f_x = sp.sympify(b0+b1*(x-x_sub_0)+b2*(x-x_sub_0)*(x-x_sub_1))

print(f_x.subs(x,3.5))