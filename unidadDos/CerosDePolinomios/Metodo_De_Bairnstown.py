import sympy as sp
import numpy as np
x=sp.symbols("x")
y=sp.symbols("y")

def bairstown(grado,coeficiente,es,s,r):
    datosBe=[]
    datosCe=[]
    datosRS=[]
    ea_r=ea_s=1000
    while ea_r>es or ea_s>es:
    #for i in range(0,1):
        be=[]
        ci=[]
        #Determinando los valores de "b"
        be.append(coeficiente[0])
        be.append(coeficiente[1]+r*be[0])
        for i in range(2,grado+1):
            be.append(coeficiente[i]+r*be[i-1]+s*be[i-2])
        #Determinando los valores de "c"
        ci.append(be[0])
        ci.append(be[1]+r*ci[0])
        for i in range(2,grado+1):
            ci.append(be[i]+r*ci[i-1]+s*ci[i-2])    
        
        #formando las ecuaciones respectivas
        #delta_R -> x , delta_S -> y
        delta = sp.solve([ci[grado-2]*x+ci[grado-3]*y+be[grado-1],ci[grado-1]*x+ci[grado-2]*y+be[grado]],[x,y])
        delta_r = delta[x]
        delta_s = delta[y]
        r = r+delta_r
        s = s + delta_s
        ea_r = abs(delta_r/r)*100
        ea_s = abs(delta_s/s)*100
        datosBe.append(be)
        datosCe.append(ci)
        datosRS.append([delta_r,delta_s,r,s,ea_r,ea_s])
    valorDeX1 = (r+sp.sqrt(r**2+4*s))/2
    valorDeX2 = (r-sp.sqrt(r**2+4*s))/2
    grado-=2
    #Comentar si da error 
    """
    datos = np.array(datosBe)
    np.savetxt("tablaVariableB.csv",datos,delimiter=",")
    datos = np.array(datosCe)
    np.savetxt("tablaVariableC.csv",datos,delimiter=",")
    datos = np.array(datosRS)
    np.savetxt("tablaVariableRS.csv",datos,delimiter=",")
    """
    return valorDeX1,valorDeX2,r,s
    

def polinomioRestante(raices,coeficiente):
    restas=[]
    factores=[]
    coeficiente2=[]
    restas2=[]
    factores2=[]
    factores.append(coeficiente[0])
    restas.append(0)
    for i in range(1,len(coeficiente)):
        restas.append(factores[i-1]*raices[0])
        factores.append(coeficiente[i]+restas[i]) 
    coeficiente2=factores
    coeficiente2.remove(coeficiente2[-1])
    factores2.append(coeficiente2[0])
    restas2.append(0)
    for i in range(1,len(coeficiente2)):
        restas2.append(factores2[i-1]*raices[1])
        factores2.append(coeficiente2[i]+restas2[i])
    return factores2


def main():
    coeficientePolinomi=[]
    grado=int(input("ingrese el grado del polinomio "))
    coeficiente=[]
    resultado=[]
    cifras=-1
    s=float(input("ingrese el valor de s "))
    r=float(input("ingrese el valor de r "))

    while cifras < 0:
        cifras = int(input("Ingrese la cantidad de cifras "))
        if cifras < 0:
            print("No se puede efectuar")
        else:
            es = 0.5*(10**(2-cifras))
    #se introduce los coeficientes
    for i in range(0,grado+1):
        coeficiente.append(float(input(f"Escriba el coeficiente del grado {grado-i}: ")))
    raices=bairstown(grado,coeficiente,es,r,s)
    grado-=2
    r=raices[2]
    s=raices[3]
    resultado.append(raices[0])
    resultado.append(raices[1])
    polinomio=polinomioRestante(raices,coeficiente)
    polinomio.remove(polinomio[-1])
    coeficientePolinomi.append(polinomio)
    while grado>=3:
        raices=bairstown(grado,polinomio,es,r,s)
        resultado.append(raices[0])
        resultado.append(raices[1])
        if grado>=3:
            r=raices[2]
            s=raices[3]
            polinomio=polinomioRestante(raices,polinomio)
            polinomio.remove(polinomio[-1])
            coeficientePolinomi.append(polinomio)
            grado-=2
    if grado==2:
        resultadoCuadratica=sp.solve(polinomio[0]*x**2+polinomio[1]*x+polinomio[2],x)
        resultado.append(resultadoCuadratica[0])
        resultado.append(resultadoCuadratica[1])
        grado-=2
    if grado==1:
        resultadoLineal=sp.solve(polinomio[0]*x+polinomio[1],x)
        resultado.append(resultadoLineal[0])
    #print(coeficientePolinomi)
    for i in resultado:
        print(i)
main()