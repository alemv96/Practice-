#date: 13 / 08 / 2017
import square

size = int(input("introduzca el tamano de su matriz cuadrada\n"))
column , row  = size , size
matrix = square.createMatrix(column , row) #inicializo la matriz
matrix = square.setValues(matrix , column , row)
square.printMatrix(matrix , row , column)

if square.analyseMatrix(matrix, column , row): print("si es un cuadrado magico")
else: print("no es un cuadrado magico")
