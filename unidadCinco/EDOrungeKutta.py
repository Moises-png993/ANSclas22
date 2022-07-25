from sympy import *
import numpy as np


def eval(valorX,valorY,funct):
    x = symbols('x')
    y = symbols('y')
    funciony = funct.subs(x,valorX)
    return float(funciony.subs(y,valorY))

def __main__():
    funcion = sympify("(x*atan(x))/y")
    xi = -1
    yi = -1
    xf = 3
    n = 20
    N = 3
    h=(xf-xi)/n
    print(h)
    tabla = []
    x = np.linspace(xi,xf, int(n+1)) 
    yf=[]  
    yf.append(yi)                                           
    fi = []
    fi.append(eval(x[0],yf[0],funcion)) 
    if N == 2:
        for i in range(1,n+1):
            k1 = eval(x[i-1],yf[i-1],funcion)
            k2 = eval(x[i-1]+h,yf[i-1]+k1*h,funcion)
            yf.append(yf[i-1]+(0.5)*(h)*(k1+k2))
        tabla=np.concatenate([[yf,x]])
        np.savetxt("RungeKuttaN2.csv",tabla,delimiter=",")
    if N==3:
        for i in range(1,n+1):
            k1 = eval(x[i-1],yf[i-1],funcion)
            k2 = eval(x[i-1]+(0.5)*h,yf[i-1]+0.5*k1*h,funcion)
            k3 = eval(x[i-1]+h,yf[i-1]-k1*h+2*k2*h,funcion)
            yf.append(yf[i-1]+(h/6)*(k1+4*k2+k3))
        tabla=np.concatenate([[yf,x]])
        np.savetxt("RungeKuttaN3.csv",tabla,delimiter=",")
    if N==4:
        for i in range(1,n+1):
            k1 = eval(x[i-1],yf[i-1],funcion)
            k2 = eval(x[i-1]+(0.5)*h,yf[i-1]+0.5*k1*h,funcion)
            k3 = eval(x[i-1]+(0.5)*h,yf[i-1]+0.5*k2*h,funcion)
            k4 = eval(x[i-1]+h,yf[i-1]+k3*h,funcion)
            yf.append(yf[i-1]+(h/6)*(k1+2*k2+2*k3+k4))
        tabla=np.concatenate([[yf,x]])
        np.savetxt("RungeKuttaN4.csv",tabla,delimiter=",")
    print(yf)
__main__()