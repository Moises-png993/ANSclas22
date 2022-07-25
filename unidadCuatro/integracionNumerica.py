import sympy as sp 


class IntegracionNumerica:

    def __init__(self,a,b,n,funcion=''):
        self.a = a
        self.b = b
        self.n = n
        self.funcion = funcion 
    
    def eval(self,valor):
        x = sp.symbols("x")
        self.funcion = sp.simplify(self.funcion)
        return float(self.funcion.subs(x,valor))

    #Regla del Trapecio N=1
    def trapecio(self):
        aproximacion = (self.b-self.a)*((self.eval(self.a)+self.eval(self.b))/2)
        return aproximacion

    #TrapecioCompuesta
    def trapecioCompuesta(self): 
        h = (self.b-self.a)/self.n
        xi = []
        suma = 0
        xi.append(self.a)
        for i in range(0,self.n+1):
            xi.append(xi[i]+h)
        for i in range(1,self.n):
            suma = suma + self.eval(xi[i])
        aproximacion = (self.b-self.a)*((self.eval(xi[0])+2*(suma)+self.eval(xi[self.n]))/(2*self.n))
        return aproximacion
    
    #Metodo Simsonp 1/3 
    def simpson_Un_Tercio(self):
        xm = (self.a+self.b)/2
        aproximacion = (self.b-self.a)*((self.eval(self.a)+4*self.eval(xm)+self.eval(self.b))/6)
        return aproximacion
    
    #Subdiviendo el intervalo en N maneras
    def simpson_Un_TercioSub(self):
        h = (self.b-self.a)/self.n
        xi = []
        xm = 0
        suma = 0
        xi.append(self.a)
        for i in range(0,self.n):
            xi.append(xi[i]+h)
        for i in range(1,self.n):
            suma = suma + self.eval(xi[i])
        for i in range(0,self.n):
            xm=xm+self.eval((xi[i]+xi[i+1])/2)
        aproximacion = (self.b-self.a)*((self.eval(xi[0])+4*xm+2*suma+self.eval(xi[self.n]))/(6*self.n))
        return aproximacion

    def simpson_Tres_Octavos(self):
        h = (self.b-self.a)/self.n
        xi = []
        xi.append(self.a)
        for i in range(0,self.n):
            xi.append(xi[i]+h)
        aproximacion = (self.b-self.a)*((self.eval(xi[0])+3*self.eval(xi[1])+3*self.eval(xi[2])+self.eval(xi[3]))/8)
        return aproximacion


#(E**((-x**2)/2))/(sqrt(2*pi))   
resultado = IntegracionNumerica(1,4,4,"(E**x)*(ln(x))")
print(resultado.trapecioCompuesta())