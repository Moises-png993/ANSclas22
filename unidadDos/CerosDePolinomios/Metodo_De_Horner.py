import numpy as np
coeficiente=[]
cifras=-1
ea=1000
valorDex=0
datos=[]
while cifras < 0:
    cifras = int(input("Ingrese la cantidad de cifras"))
    if cifras < 0:
        print("No se puede efectuar")
    else:
        es = 0.5*(10**(2-cifras))

#introducimos la cantidad de grados y sumamos uno
grado =int(input("ingrese el grado de polinomio deseado: " ))
#introducimos el valor inicial
x_Inicial=float(input("ingrese el valor inical deseado"))

for i in range(0,grado+1): #for(i=0;i<grado;i++)
    coeficiente.append(float((input(f"Escriba el coeficiente del grado {grado-i}: "))))
while ea > es:
    restas=[]
    factores=[]
    coeficiente2=[]
    restas2=[]
    factores2=[]
    #le heredamos el primer elemento de los coeficientes a factores
    factores.append(coeficiente[0])
    #para evitar el index error agregamos un 0 en el inicio 
    restas.append(0)
    for i in range(1,len(coeficiente)):
        #multiplicamos cada factor con el valor 
        restas.append(factores[i-1]*x_Inicial)
        #Restamos cada valor para poder obtener nuevamente los factores
        factores.append(coeficiente[i]+restas[i])
    #guardamos el valor de R 
    R=factores[-1]
    coeficiente2=factores
    coeficiente2.remove(coeficiente2[-1])
    factores2.append(coeficiente2[0])
    restas2.append(0)
    for i in range(1,len(coeficiente2)):
        restas2.append(factores2[i-1]*x_Inicial)
        factores2.append(coeficiente2[i]+restas2[i])
    S=factores2[-1]
    datos.append(R)
    datos.append(S)
    datos.append(x_Inicial)
    valorDex=x_Inicial-R/S
    ea=abs((valorDex-x_Inicial)/valorDex)*100
    x_Inicial=valorDex
datos = np.array(datos)
np.savetxt("tablaDeIteraciones.csv",datos,delimiter=",")
print(valorDex)
print(ea)
