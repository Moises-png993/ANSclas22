import sympy as sp
#Calcular dado valores de X y una funcion
x = sp.symbols('x')
grado = int(input("Ingrese el grado: "))
funcion = sp.sympify(input("Ingrese la funcion a evaluar: "))
valor_x = []
valor_y = []
for i in range(0,grado+1):
    valor_x.append(float(input(f"Ingrese el valor de x{i}: ")))
    valor_y.append(float(funcion.subs(x,valor_x[i])))
if grado == 1:
    polinomio=sp.sympify(((valor_y[1]-valor_y[0])/(valor_x[1]-valor_x[0]))*(x-valor_x[0])+valor_y[0])
if grado == 2:
    b0 = valor_y[0]
    b1 = (valor_y[1]-valor_y[0])/(valor_x[1]-valor_x[0])
    b2 = ((valor_y[2]-valor_y[1])/(valor_x[2]-valor_x[1]) - (valor_y[1]-valor_y[0])/(valor_x[1]-valor_x[0]))/(valor_x[2]-valor_x[0])
    polinomio=sp.sympify(b0+b1*x-b1*valor_x[0]+b2*x**2-b2*valor_x[1]*x-b2*valor_x[0]*x+b2*valor_x[0]*valor_x[1])
    print(polinomio)