import numpy as np
while True:
    try:
        V=int(input("¿Cuantas variables de entrada se utilizaran?(Solo digitos enteros): " ))
        break
    except ValueError:
        print("Error. Solo se pueden ingresar digitos enteros!")

Init = np.zeros((V))
MatPro = np.zeros((V,V))
NeMatPro = np.zeros((V,V))
Result = np.zeros((V))


#Se declaran cuantos datos son de entrada
for i in range (0,V):
    while True:
        try:
            Add=float(input("Ingrese el valor " + str(i+1) + " (Solo digitos): " ))
            break
        except ValueError:
            print("Error. Solo se pueden ingresar digitos")
    Init[i]= Add

# Se declaran las probabilidades de cambiar entre los estados en porcentajes     
for i in range (0,V):
    for j in range (0,V):
        if(i == j):
           while True:
                try:
                    Add=float(input("¿Cual es la probabilidad de que la variable se mantenga en su mismo estado?(Ingresar los valores como digitos y porcentajes sin el simbolo %): "))
                    if(Add >100 or Add < 0):
                        print("Solo se pueden ingresar porcentajes entre 0 y 100!")
                    else:    
                        MatPro[i][j] = Add/100
                        break
                except ValueError:
                    print("Error. Solo se pueden ingresar digitos!")  
        else:    
            while True:
                try:
                    Add=float(input("¿Cual es la probabilidad de que la variable " + str(i+1) + " cambie de estado a la variable " + str(j+1) + "?(Ingresar los valores como digitos y porcentajes sin el simbolo %): "))
                    if(Add>100 or Add < 0):
                        print("Solo se pueden ingresar valores entre 0 y 100!")
                    else:    
                        MatPro[i][j] = Add/100
                        break
                except ValueError:
                    print("Error. Solo se pueden ingresar digitos!")
            

# Se declaran cuantas iteraciones se quieren llevar a cabo
while True:
    try:
        It = int(input("¿Cuantas iteraciones le gustaria que se lleven a cabo?(Ingresar digito entero): "))
        if(It<=0):
            print("Error. Las iteraciones tienen que ser mayores a 0!")
        else:    
            break
    except ValueError:
        print("Error. Solo se pueden ingresar digitos enteros")        

if(It > 1):
    # Iteraciones llevadas a cabo
    for a in range (0,It-1):
        #Indices de los valores
        for i in range (0,V):
            for j in range (0,V):
                #Limitador de la sumatoria (K)
                for k in range (0,V):
                    NeMatPro[i][j]=NeMatPro[i][j]+MatPro[i][k]*MatPro[k][j]
        #Se empujan los valores de la matriz temporal a la original y se limpia la matriz temporal
        for i in range (0,V):
            for j in range (0,V):
                MatPro[i][j] = NeMatPro[i][j]
                NeMatPro[i][j] = 0

#Se calculan los valores de salida
for i in range (0,V):
    for j in range (0,V):
        Result[i]= Result[i]+(Init[j]*MatPro[j][i])


#Impresion de valores de salida
print("\nValores de entrada.")
print(Init)
print("\nValores de matriz de probabilidades.")
print(MatPro)
print("\nValores de salida a " +str(It)+" meses. ")
print(Result)
