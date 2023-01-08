import Calculator
import Eqn

#menu de usuario
#while dataEntry != 5:
print("1- Suma")
print("2- resta ")
print("3- multiplicacion")
print("4- division ")
print("5- ecuacion de segundo grado")
#puedo colocar otras opciones como ecuaciones de segundo grado etc
dataEntry = int(input())
if dataEntry == 1 :
    print("introduzca los valores a sumar: \n")
    number1 = int(input("numero 1 \n"))
    number2 = int(input("numero 2 \n"))
    print("la suma de los valores es: " , Calculator.Suma(number1 , number2))
elif dataEntry == 2:
    print("introduzca los valores a restar: \n")
    number1 = int(input("numero 1 \n"))
    number2 = int(input("numero 2 \n"))
    print("la resta de los valores es: " , Calculator.Resta(number1 , number2))
elif dataEntry == 3:
    print("introduzca los valores a multiplicar: \n")
    number1 = int(input("numero 1 \n"))
    number2 = int(input("numero 2 \n"))
    print("la multiplicacion de los valores es: " , Calculator.Multiplicacion(number1 , number2))
elif dataEntry == 4:
    print("introduzca los valores a dividir: \n")
    number1 = int(input("numero 1 \n"))
    number2 = int(input("numero 2 \n"))
    print("la Division de los valores es: " , Calculator.Division(number1 , number2))
else:
    print("introduzca los coheficientes")
    number1 = int(input("coheficiente 1 \n"))
    number2 = int(input("coheficiente 2 \n"))
    number3 = int(input("coheficiente 3 \n"))
    Eqn.secondGradeEquation(number1 , number2 , number3)
