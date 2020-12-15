import numpy as np
from os import system, name
from time import sleep
from simplex import Simplex

#Funcion para limpiar la consola :)
def clear():
    if  name=='nt':
        _=system('cls')
    else:
        _=system('clear')

#Funcion para maximizar 
def SMaximizar():
    #Convertir funcion objetivo de int a un string
    for i in range(0,var):
        if(i==0):
            obj= str(int(Fun[i]))+"x_"+str(i+1)
        elif(i>0):
            obj= str(obj)+" + "+str(int(Fun[i]))+"x_"+str(i+1)
    
    #Se declara la funcion objetivo para el solver
    objective= ('maximize', str(obj))

    #Convertir los constraints de ints a strings (deben de ser listas)
    
    for i in range (0,res):
        for j in range (0,var+2):
            # Conversion de coeficientes
            if(j<var):
                if(j==0):
                    Cons[i]=str(int(Rest[i][j]))+"x_"+str(j+1)
                elif(j>0):
                    Cons[i]=Cons[i] +" + "+ str(int(Rest[i][j]))+"x_"+str(j+1)
            #Conversion de tipo de restriccion    
            elif(j==var):
                if(Rest[i][j]==1):
                    Cons[i]= Cons[i]+" <= "
                if(Rest[i][j]==2):
                    Cons[i]= Cons[i]+" >= "
                if(Rest[i][j]==3):
                    Cons[i]= Cons[i]+" = "        
            #Conversion de limitador de restriccion    
            elif(j>=var):
                Cons[i]=Cons[i]+str(int(Rest[i][j]))    
    constraints= Cons            
    Lp_system = Simplex(num_vars=var,constraints=constraints,objective_function=objective)
    print(Lp_system.solution)
    print(Lp_system.optimize_val)
    #print(Cons)
    #print(obj)
   
    

#Funcion para minimizar 
def SMinimizar():
     #Convertir funcion objetivo de int a un string
    for i in range(0,var):
        if(i==0):
            obj= str(int(Fun[i]))+"x_"+str(i+1)
        elif(i>0):
            obj= str(obj)+" + "+str(int(Fun[i]))+"x_"+str(i+1)
    
    #Se declara la funcion objetivo para el solver
    objective= ('minimize', str(obj))

    #Convertir los constraints de ints a strings (deben de ser listas)
    
    for i in range (0,res):
        for j in range (0,var+2):
            # Conversion de coeficientes
            if(j<var):
                if(j==0):
                    Cons[i]=str(int(Rest[i][j]))+"x_"+str(j+1)
                elif(j>0):
                    Cons[i]=Cons[i] +" + "+ str(int(Rest[i][j]))+"x_"+str(j+1)
            #Conversion de tipo de restriccion    
            elif(j==var):
                if(Rest[i][j]==1):
                    Cons[i]= Cons[i]+" <= "
                if(Rest[i][j]==2):
                    Cons[i]= Cons[i]+" >= "
                if(Rest[i][j]==3):
                    Cons[i]= Cons[i]+" = "        
            #Conversion de limitador de restriccion    
            elif(j>=var):
                Cons[i]=Cons[i]+str(int(Rest[i][j]))    
    constraints= Cons            
    Lp_system = Simplex(num_vars=var,constraints=constraints,objective_function=objective)
    print(Lp_system.solution)
    print(Lp_system.optimize_val)
    #print(Cons)
    #print(obj)
   
    


#Declaracion inicial de valores de problema
while True:
    try:
        var = int(input("¿Cuantas variables de desicion tiene el problema?(Introducir solo digitos enteros): "))
        break
    except ValueError:
        print("Error. Solo se pueden ingresar digitos enteros!") 
while True:
    try:
        res = int(input("¿Cuantas restricciones tiene el problema?(Introducir solo digitos enteros): "))
        break
    except ValueError:
        print("Error. Solo se pueden ingresar digitos enteros!") 

clear()

while True:
    try:
        typ = int(input("¿Cual es el objetivo de la funcion? \n 1.- Maximizar\n 2.- Minimizar \n"))
        if(typ!= 1 and typ!= 2 ):
            print("Error. Solo se pueden seleccionar los valores previamente establecidos!")
        else:
            break    
    except:
        print("Error. Solo se pueden ingresar digitos enteros!")     

#Se ingresan los datos al arreglo de Funcion
clear()
Fun = np.zeros((var))

#FunVars almacena los valores de resultado por variable en Z
FunVars = np.zeros((var))

for i in range (0,var):
    while True:
        try: 
            Fun[i]= float(input("Ingresar el valor de X"+ str(i+1)+ ": "))
            break
        except ValueError:
            print("Error. Solo se pueden ingresar digitos!")

#Se ingresan los datos a las restricciones
Rest = np.zeros((res,var+2))
Cons=[]
for i in range (0,res):
    Cons.append('')

for i in range (0,res):
    for j in range (0,var+2):
        #Aqui se ingresan los datos 
        if(j<var):
             while True:
                try:
                    Rest[i][j]= float(input("Ingresar el valor de X" + str(j+1)+" en la restriccion numero " + str(i+1)+ ": "))
                    if(Rest[i][j]<0):
                        print("Error. Solo se pueden ingresar valores mayores a 0")
                    else:    
                        break
                except ValueError:
                    print("Error. Solo se pueden ingresar digitos!")    

        #Aqui se ingresa el tipo de restriccion    
        elif(j==var):
            while True:
                try:
                    print("Ingresar el tipo de restriccion de la restriccion numero "+str(i+1)+ "\n 1.- <= \n 2.- >= \n 3.- = ")
                    Rest[i][j]=int(input("Tipo: "))
                    if(Rest[i][j]!=1 and Rest[i][j]!=2 and Rest[i][j]!=3):
                        print("Error. Solo se pueden ingresar digitos entre 1 y 3!")
                    else:
                        break    
                except ValueError:
                    print("Error. Solo se pueden ingresar digitos enteros!")    
        #Aqui se ingresa el valor de la restriccion    
        elif(j==var+1):
            while True:
                try:
                    Rest[i][j]= float(input("Ingresar el valor final de la restriccion numero "+str(i+1)+": "))
                    if(Rest[i][j]<0):
                        print("Error. No se pueden ingresar valores menores a 0 en las restricciones!") 
                    else:
                        break   
                except ValueError:
                    print("Error. Solo se pueden ingresar digitos!")
clear()
#Restriccion de binarios
while True:
    try:
        bins= int(input("¿Las soluciones tienen que ser binarias? \n 1.- Si \n 2.- No \n"))
        if(bins!=1 and bins!=2):
            print("Error. Solo se pueden ingresar los valores anteriormente especificados!")
        else:
            break
    except ValueError:
        print("Error. Solo se pueden ingresar digitos enteros!")
#Restriccion de enteros
clear()
while True:
    try:
        ints= int(input("¿Las soluciones tienen que ser enteros? \n 1.- Si \n 2.- No \n"))
        if(ints!=1 and ints!=2):
            print("Error. Solo se pueden ingresar los valores anteriormente especificados!")
        else:
            break
    except ValueError:
        print("Error. Solo se pueden ingresar digitos enteros!")

#Se llaman las funciones para maximizar o minimizar

if(typ==1):
    SMaximizar()

elif(typ==2):
    SMinimizar()
