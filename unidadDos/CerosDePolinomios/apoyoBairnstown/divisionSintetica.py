
raices=[-1,-9]
coeficiente=[1,27,269,1197,2250,1296]
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
polinomio=polinomioRestante(raices,coeficiente)
print(polinomio)
