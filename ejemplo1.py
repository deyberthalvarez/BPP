"""
Presentado por DEYBERTH ALVAREZ
Haciendo uso de comprensión de listas realice un programa que, dado una lista de listas de números enteros, devuelva el máximo de cada lista. Por ejemplo, suponga la siguiente listas de listas:
[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

"""
#import pdb
#pdb.set_trace()
lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
[print(max(i)) for i in lista]

"""
2. Haga uso de la función filter para construir un programa que,
dado una lista de n números devuelva aquellos que son primos. Por ejemplo, 
dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente debe devolver como 
resultado [3, 5, 5, 13]
"""
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

