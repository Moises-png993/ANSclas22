from sympy import *
import numpy as np


def eval(valorX,valorY,funct):
    x = symbols('x')
    y = symbols('y')
    funciony = funct.subs(x,valorX)
    return float(funciony.subs(y,valorY))

def __main__():
    funct= sympify("(y**2)*(sin(x**2))")
    xi = -2
    yi = 1/3
    xf = 2
    n = 20
    h=(xf-xi)/n
    print(h)
    tabla = []
    x = np.linspace(xi,xf, int(n+1))      
    print(x)                          
    yf=[]  
    yf.append(yi)                                           
    fi = []
    fi.append(eval(x[0],yf[0],funct)) 
    for i in range(1,n+1):
        yf.append(yf[i-1]+h*fi[i-1])
        yf[i]=yf[i-1]+h*((eval(x[i-1],yf[i-1],funct)+eval(x[i],yf[i],funct))/2)
        fi.append(eval(x[i],yf[i],funct))

    tabla=np.concatenate([[yf,x]])
    np.savetxt("Euler.csv",tabla,delimiter=",")
    print(yf)
__main__()