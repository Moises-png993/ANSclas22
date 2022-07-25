import sympy as sp
import numpy as np

class tartaglia:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c       
    def resultado(self):
        p=(3*self.b-(self.a**2))/3
        q=((2*self.a**3)-9*self.a*self.b+27*self.c)/27
        delta=((q/2)**2)+((p/3)**3)
        if delta==0:
            if p ==0 and q==0:
                x_Uno=(-self.a/3)
            else: 
                x_Uno=-(3*q)/(2*p) - self.a/3
        elif delta > 0: 
            x_Uno=np.cbrt(-(q/2)+ np.sqrt(delta)) + np.cbrt(-(q/2)- np.sqrt(delta)) - (self.a/3)
        elif delta < 0:
            teta=sp.acos(-(q/2)/np.sqrt(-(p/3)**3))
            x_Uno=2*sp.sqrt(-(p/3))*sp.cos((teta+2*0*sp.pi)/3)-(self.a/3)
        return x_Uno    