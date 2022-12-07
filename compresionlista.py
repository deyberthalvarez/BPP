""" compresión de lista
summary_
    Definir una lista con 5 valores enteros,
    luego a partir de la primer lista generar una segunda lista con los valores elevados al cuadrado.
"""
lista1=[8, 5, 4, 10, 2]
lista2=[]
for elemento in lista1:
    lista2.append(elemento*elemento)
print("Lista 1")    
print(lista1)
print("Nueva lista")
print(lista2)

"""_summary_
    Se tiene una lista con un conjunto de tuplas con los nombres y edades de personas:
    Generar una lista con las personas mayores de edad.
"""
personas=[('pedro',33),('ana',3),('juan',13),('carla',45)]
personas_mayores=[per for per in personas if per[1]>=18]
print(personas_mayores)

listaenteros=[8, 5, 4, 10, 2]
mayor=[]
print("recorrer una lista por indice")  
# recorrer una lista por indice
for indice in range(len(listaenteros)):
    print(listaenteros[indice])
    
print("imprimir lista por valores")    
# Por los valores de la lista.   
for numero in listaenteros:
    print(numero)
 
 
lista=[8, 5, 4, 10, 2]    
maximo = lista[0]
for i in range(1, len(lista)):
    if lista[i] > maximo:
        maximo = lista[i]
        

#lista_de_maximos.append(maximo)
print("maximo")
print(maximo)    

max = sorted(lista)[-1]
print("maximo de max:", max)

def max(a):

    res = a[0]
    for i in a:
        if res < i:
            res = i
    return res

array = (1, 2, 3, 4, 5, 6)

print("maximo utilizando la función:",max(array))

#my_list = [0, 2, 5, 6, 5, 8, 5, 8, 8]
#my_max = [0]
#list=len(my_list)
#for list in my_list:
#    if list > 7:
#       my_max=my_max+ my_list[list]
#print("mayor de 7 :",my_max)

print("maximo utilizando indice de s:")
s=[10,11,12,9,10,11]
length = len(s)-1
for i in range(length):
    if s[i] > s[i + 1]:
        s[i], s[i + 1] = s[i + 1], s[i]
print(s[-1]) #12
#def max_lista(lista):
#return [mayor_lista(subl) for subl in l]


print("maximo utilizando indice de arr:")

arr=[10,11,12,9,10,11]

#Find the length of you list
len=len(arr) 

#Use 1st for loop to iterate over index from 0 to total length
for i in range(len):
   # Use 2nd for loop to iterate from from index 1 to total length
   for j in range(i+1,len):
    #Compare 1st index to next index
    if arr[i]>arr[j]:
        #replace the positions to sort our max number at last
        arr[i],arr[j]=arr[j],arr[i]
 # Now, your sorted list having last element as a max for access it with index -1 (last index) of list, You will get max number from your list without using max() function
print("Your max number is:",arr[-1])

#El siguiente código de ejemplo muestra cómo recorrer una lista y eliminar 
# números impares usando la comprensión de listas en Python.
mylist = [1,4,7,8,20]

newlist = [x for x in mylist if x%2 == 0]
print(newlist)

#Crear una lista de pares a partir de otra lista creada con las potencias de 2 de los primeros 10 números:

# Método tradicional
lista = []
for numero in range(0,11):
    lista.append(numero**2)

pares = []   
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)
#compresion lista
lista = [numero for numero in 
            [numero**2 for numero in range(0,11)] 
                if numero % 2 == 0 ]
print(lista)

#lista de lista
print("lista de lista")
lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

for sublista in lista:
    max_values = max(sublista)
    print(max_values)

#maxValues = [max(i) for i in lista]
#lista numero mayor 
print("lista numero mayor")
print("lista", lista)
[print(max(i)) for i in lista]



print("lista numeros multiples de un numero")

def multiple(numero):    # Primero declaramos una función condicional
    if numero % 5 == 0:  # Comprobamos si un numero es múltiple de cinco
        return True      # Sólo devolvemos True si lo es

numeros = [2, 5, 10, 23, 50, 33]

multiple=list(filter(multiple, numeros))
print ("multiple", multiple)

multiple2=list(filter(lambda numero: numero%5 == 0, numeros) )
print ("multiple2", multiple2)
print("lista numeros primos")

import math
 
def es_primo(numero):
    """
    Funcion que determina si un numero es primo
    Tiene que recibir el numero entero
    """
    # Para que un numero sea primo, unicamente tiene que dividirse dos veces:
    #   1 - divisible entre 1
    #   2 - divisible entre el mismo
    # En este bucle, empezamos por el dos hasta un numero anterior a el, por lo
    # que si en el bucle, alguna vez se divide el numero, quiere decir que no es
    # primo
    if (numero<=1):
        return False
 
    for i in range(2, math.ceil(math.sqrt(numero))+1):
        if(numero%i==0 and i!=numero):
            return False
    return True
 
lista = [3, 4, 8, 5, 5, 22, 13]
nuevaLista=list(filter(lambda x: es_primo(x), lista))
print(nuevaLista)


print("imprmir los numeros primos que hay hasta el numero")
def f(n):
    return all([not n%x==0 for x in range(2,n)])

for i in range(2,20):
    print(i,f(i))
    
def g(n):
    for i in range(2,n):
        if f(i):
                print(i)
                
g(30)     