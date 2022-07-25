#Dado dos puntos se puede determinar un punto de forma lineal
x_sub_cero = float(input("Introduzca el valor de X0: "))
y_sub_cero = float(input("Introduzca el valor de Y0: "))
x = float(input("Introduzca el valor de X: "))
x_sub_uno = float(input("Introduzca el valor de X1: "))
y_sub_uno = float(input("Introduzca el valor de Y1: "))


P_X = y_sub_cero+((y_sub_uno-y_sub_cero)/(x_sub_uno-x_sub_cero))*(x-x_sub_cero)

print("El valor buscado es: ",P_X)