from sympy import *
import numpy as np

def eval(valorX,valorY,funct):
    x = symbols('x')
    y = symbols('y')
    funciony = funct.subs(x,valorX)
    return float(funciony.subs(y,valorY))

def __main__():
    funcion = sympify("(y*cos(x))/(3*x)")
    xi = 1
    yi = 0
    xf = 3
    n = 10
    N = 4
    h=(xf-xi)/n
    print(h)
    tabla = []
    x = np.linspace(xi,xf, int(n+1)) 
    evalu = []
    yf=[]  
    yf.append(yi)                                           
    fi = []
    fi.append(eval(x[0],yf[0],funcion)) 
    if N==4:
        for i in range(1,4):
            k1 = eval(x[i-1],yf[i-1],funcion)
            k2 = eval(x[i-1]+(0.5)*h,yf[i-1]+0.5*k1*h,funcion)
            k3 = eval(x[i-1]+(0.5)*h,yf[i-1]+0.5*k2*h,funcion)
            k4 = eval(x[i-1]+h,yf[i-1]+k3*h,funcion)
            yf.append(yf[i-1]+(h/6)*(k1+2*k2+2*k3+k4))
    contador = 0
    for i in range(4,n+1):
        for j in range(contador,contador+4):
            evalu.append(eval(x[j],yf[j],funcion))
        yf.append(yf[i-1]+(h/24)*(55*evalu[3]-59*evalu[2]+37*evalu[1]-9*evalu[0]))
        evalu.append(eval(x[i],yf[i],funcion))
        yf[i]=( yf[i-1] + (h/24)*(9*evalu[4]+19*evalu[3]-5*evalu[2]+evalu[1]))
        evalu.clear()
        contador+=1
    tabla=np.concatenate([[yf,x]])
    np.savetxt("multipasos.csv",tabla,delimiter=",")
    print(yf)
__main__()