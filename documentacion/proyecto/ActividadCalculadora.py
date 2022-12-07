
"""
Crea una clase calculadora que pueda ser utilizada de la siguiente manera
calculadora = calculadora(num1, num2)
calculadora.sumar()
calculadora.multiplicar()
calculadora.restar()
calculadora.dividir().
"""



class Calculadora():
    """ LA clase calculadora 
    los parametros numero1, numero2.
    """
    def __init__(self,numero1,numero2):
        self.numero1=numero1
        self.numero2=numero2
    
        
    
    def sumar(self):
        """la funcion sumar
        :param func: Function to process.
        :type func: Callable.
        :param args: Arguments for the function to process.
        :type args: int.
        :returns: Int.
        :rtype: Int.
        """
        resultado = self.numero1 + self.numero2
        
        print("la suma de ", self.numero1," + ",self.numero2," = " ,resultado)
        
    def resta(self):
        """función restar.
        """
        resultado=resultado = self.numero1 - self.numero2   
        print("la resta de ", self.numero1," - ",self.numero2," = " ,resultado)
        
    def multiplicacion(self):
        """funcion multiplicar
        :parametro numero1 int
        :parametro numero2 int
        :return: Int.
        """
        resultado = self.numero1 * self.numero2   
        print("la multiplicacion de ", self.numero1," * ",self.numero2," = " ,resultado) 
         
    def division(self):
        """funcion division
        :parametro numero1 int
        :parametro numero2 int
        la excepcion es el numero2 no debe ser cero
        """
        try:
          resultado =self.numero1/self.numero2
          print("La division de ", self.numero1, " / ",self.numero2 ," = ", resultado)
        except Exception:
          print("No se puede dividir por cero!\n")
                     
opcion1=input("Desea Realizar una operación Matematica: S/N ") 
opcionmn=opcion1.upper()
if opcionmn != "S":
    print("Debe ser la tecla S/s")
    quit()
               
while(opcionmn == "S" ):
    
    try:
        num1=int(input("Digite Numero 1:"))
        num2=int(input("Digite Numero 2:"))
        MiCalculadora=Calculadora(num1,num2)
        print("El numero 1: ",MiCalculadora.numero1)
        print("El numero 2: ",MiCalculadora.numero2)
            # otra manera sin utilizar un menu
            #MiCalculadora.sumar()
            #MiCalculadora.resta()
            #MiCalculadora.multiplicacion()
            #MiCalculadora.division()
    
        opcion=int(input("Digite\n numero: 1 Suma\n numero: 2 Resta\n Numero: 3 Multipliacion\n Numero: 4 Division\n Opcion: "))
        if opcion == 1:
         MiCalculadora.sumar()
        elif opcion == 2:        
            MiCalculadora.resta()
        elif opcion ==3 :  
            MiCalculadora.multiplicacion()
        elif opcion == 4 :               
            MiCalculadora.division()
        else :             
            print("opcion invalida")
    except Exception:
 
        print ("Debes Insertar solamente Numeros!\n")
    opcion1=input("Desea Realizar otra operación Matematica: S/N ")
    opcionmn=opcion1.upper()    
   
