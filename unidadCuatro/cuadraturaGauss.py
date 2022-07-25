import sympy as sp 
def eval(valor):
    funcion = sp.sympify("((E**x)*sin(x))/(1+x**2)")
    x = sp.symbols("x")
    funcion = sp.simplify(funcion)
    return float(funcion.subs(x,valor))
#un punto 
w_uno = [2.0]
k_uno = [0.0]
#Dos puntos
w_dos = [1.0,1.0]
k_dos = [-0.57735,0.57735]
#Tres puntos
w_tres = [0.555556,0.888889,0.555556]
k_tres = [-0.774597,0.0,0.774597]
#Cuatro Puntos
w_cuatro = [0.347855,0.652145,0.652145,0.347855]
k_cuatro = [-0.861136,-0.339981,0.339981,0.861136]
#cinco Puntos
w_cinco = [0.236927,0.478629,0.568889,0.478629,0.236927]
k_cinco = [-0.90618,-0.538469,0.0,0.538469,0.90618]

x = sp.symbols("x")
a = int(input("Ingrese el limite a: "))
b = int(input("Ingrese el limite b: "))
puntos = int(input("Ingrese el punto de gauss: "))
if puntos == 1:
    aproximacion = ((b-a)/2)*(eval(w_uno[0]*(((b-a)*k_uno[0]+(b+a))/2)))
if puntos == 2:
    #eval(w_dos[0]*(((b-a)*k_dos[0]+(b+a))/2))
    aproximacion =((b-a)/2)*(w_dos[0]*eval((((b-a)*k_dos[0]+(b+a))/2))+w_dos[1]*eval((((b-a)*k_dos[1]+(b+a))/2)))
if puntos == 3:
    #eval(w_tres[0]*(((b-a)*k_tres[0]+(b+a))/2)
    aproximacion = ((b-a)/2)*(w_tres[0]*eval(((b-a)*k_tres[0]+(b+a))/2)+w_tres[1]*eval(((b-a)*k_tres[1]+(b+a))/2)+w_tres[2]*eval(((b-a)*k_tres[2]+(b+a))/2))
print(aproximacion)