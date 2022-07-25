from sympy import *
import numpy as np

def eval(valorX,valorY,funcion=""):
    x = symbols('x')
    y = symbols('y')
    funciony = funcion.subs(x,valorX)
    return float(funciony.subs(y,valorY))

def __main__():
    funct= sympify("(x*atan(x))/y")
    dly1= sympify("(atan(x)/y)+(x/(y*(x**2+1)))")
    dly2= sympify("2/(y*(x**2+1)**2)")
    dly3= sympify("(-8*x)/(y*(x**2+1)**3)")
    dly4 = sympify("(8*(5*x**2-1))/(y*(x**2+1)**4)")
    xi = 0
    yi = 3
    xf = 5
    n = 25
    N = 5
    h=(xf-xi)/n
    tabla =[]
    x = np.linspace(xi,xf, int(n+1))  
    if N == 2:
        yf=[]
        yf.append(yi)                                           
        fi = []
        T = h*(eval(x[0],yf[0],funct)+(h/2)*eval(x[0],yf[0],dly1))
        fi.append(T)
        for i in range(1,n+1):
            yf.append(yf[i-1]+fi[i-1])
            T = h*(eval(x[i],yf[i],funct)+(h/2)*eval(x[i],yf[i],dly1))
            fi.append(T)
        tabla=np.concatenate([[yf,x]])
        np.savetxt("EDOtaylorN2.csv",tabla,delimiter=",")
    if N==3: 
        yf=[]
        yf.append(yi)                                           
        fi = []
        T = h*(eval(x[0],yf[0],funct)+(h/2)*eval(x[0],yf[0],dly1)+((h**2)/6)*eval(x[0],yf[0],dly2))
        fi.append(T)
        for i in range(1,n+1):
            yf.append(yf[i-1]+fi[i-1])
            T = h*(eval(x[i],yf[i],funct)+(h/2)*eval(x[i],yf[i],dly1)+((h**2)/6)*eval(x[i],yf[i],dly2))
            fi.append(T)
        tabla=np.concatenate([[yf,x]])
        np.savetxt("EDOtaylorN3.csv",tabla,delimiter=",")
    if  N==4:
        yf=[]
        yf.append(yi)                                           
        fi = []
        T = h*(eval(x[0],yf[0],funct)+(h/2)*eval(x[0],yf[0],dly1)+((h**2)/6)*eval(x[0],yf[0],dly2)+((h**3)/24)*eval(x[0],yf[0],dly3))
        fi.append(T)
        for i in range(1,n+1):
            yf.append(yf[i-1]+fi[i-1])
            T = h*(eval(x[i],yf[i],funct)+(h/2)*eval(x[i],yf[i],dly1)+((h**2)/6)*eval(x[i],yf[i],dly2)+((h**3)/24)*eval(x[i],yf[i],dly3))
            fi.append(T)
        tabla=np.concatenate([[yf,x]])
        np.savetxt("EDOtaylorN4.csv",tabla,delimiter=",")
    if N==5: 
        yf=[]
        yf.append(yi)                                           
        fi = []
        T = h*(eval(x[0],yf[0],funct)+(h/2)*eval(x[0],yf[0],dly1)+((h**2)/6)*eval(x[0],yf[0],dly2)+((h**3)/24)*eval(x[0],yf[0],dly3)+((h**4)/120)*eval(x[0],yf[0],dly4))
        fi.append(T)
        for i in range(1,n+1):
            yf.append(yf[i-1]+fi[i-1])
            T = h*(eval(x[i],yf[i],funct)+(h/2)*eval(x[i],yf[i],dly1)+((h**2)/6)*eval(x[i],yf[i],dly2)+((h**3)/24)*eval(x[i],yf[i],dly3)+((h**4)/120)*eval(x[i],yf[i],dly4))
            fi.append(T)
        tabla=np.concatenate([[yf,x]])
        np.savetxt("EDOtaylorN5.csv",tabla,delimiter=",")
__main__()