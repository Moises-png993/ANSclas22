import sympy as sp 


funcion = sp.sympify("(8*(5*x**2-1))/(y*(x**2+1)**4)")
def eval(valorX,valorY,funct):
    x = sp.symbols('x')
    y = sp.symbols('y')
    funciony = funct.subs(x,valorX)
    return float(funciony.subs(y,valorY))
print(eval(2,2,funcion))