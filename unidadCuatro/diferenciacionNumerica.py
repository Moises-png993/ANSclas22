import sympy as sp

class DiferenciaNumerica:

    def __init__(self,x0,h,funcion=''):
        self.x0 = x0
        self.h = h
        self.funcion = funcion 

    def eval(self,valor):
        x = sp.symbols("x")
        self.funcion = sp.simplify(self.funcion)
        return float(self.funcion.subs(x,valor))
        
    def valorReal(self,valor):
        x = sp.symbols("x")
        self.funcion = sp.simplify(self.funcion)
        derivada = self.funcion.diff(x)
        return float(derivada.subs(x,valor))

    def divUnoAdelante(self):
        aproximacion = float((self.eval(self.x0+self.h)-self.eval(self.x0))/self.h)
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error

    def divDosAdelante(self):
        aproximacion = float((-self.eval(self.x0+2*self.h)+4*self.eval(self.x0+self.h)-3*self.eval(self.x0))/(2*self.h))
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error

    def divUnoAtras(self):
        aproximacion = float((self.eval(self.x0)-self.eval(self.x0-self.h))/self.h)
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error 
    
    def divDosAtras(self):
        aproximacion = float((3*self.eval(self.x0)-4*self.eval(self.x0-self.h)+self.eval(self.x0-2*self.h))/(2*self.h))
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error

    def divCentral(self):
        aproximacion = float((self.eval(self.x0+self.h)-self.eval(self.x0-self.h))/(2*self.h))
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion

    def divOrden4(self):
        aproximacion = float((-self.eval(self.x0+2*self.h)+(8)*self.eval(self.x0+self.h)-(8)*(self.eval(self.x0-self.h))+self.eval(self.x0-2*self.h))/(12*self.h))
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error
    
    def divTresPuntos1(self):
        aproximacion = float((self.eval(self.x0+self.h)-self.eval(self.x0-self.h))/(2*self.h))
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error

    def divTresPuntos2(self):
        aproximacion = float( (-3*self.eval(self.x0)+4*self.eval(self.x0+self.h)-self.eval(self.x0+2*self.h))/(2*self.h))
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error
    
    def divCincoPuntos1(self):
        aproximacion = float((1/(12*self.h))*((-25)*(self.eval(self.x0))+(48)*(self.eval(self.x0+self.h))-(36)*(self.eval(self.x0+2*self.h))+(16)*(self.eval(self.x0+3*self.h))-(3)*self.eval(self.x0+4*self.h)))
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error

    def divCincoPuntos2(self):
        aproximacion = float((1/(12*self.h))*((-3)*(self.eval(self.x0-self.h))-(10)(self.eval(self.x0))+(18)*(self.eval(self.x0+self.h))-(6)*(self.eval(self.x0+self.h))+(self.eval(self.x0+3*self.h))))
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error

    def divCincoPuntos3(self):
        aproximacion =  float((-self.eval(self.x0+2*self.h)+(8)*self.eval(self.x0+self.h)-(8)*(self.eval(self.x0-self.h))+self.eval(self.x0-2*self.h))/(12*self.h))
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error

    def divCincoPuntos4(self):
        aproximacion = float((1/(12*self.h))*((4)*(self.eval(self.x0-3*self.h))+(6)*(self.eval(self.x0+2*self.h))-(8)*(self.eval(self.x0-self.h))+(34)*(self.eval(self.x0))+(3)*(self.eval(self.x0+self.h))+(34)*(self.eval(self.x0))))
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error
    
    def divCincoPuntos5(self):
        aproximacion = float((1/(12*self.h))*((self.eval(self.x0-4*self.h))-(3)*(self.eval(self.x0-3*self.h))+(4)*(self.eval(self.x0-2*self.h))-(36)*(self.eval(self.x0-self.h))+(25)*(self.x0)))
        error = abs((self.valorReal(self.x0)-aproximacion)/self.valorReal(self.x0))
        return aproximacion,error
    

resultado = DiferenciaNumerica(0.65,0.2,"x**3*E**(x**2)+cos(x)")
print(resultado.funcion())