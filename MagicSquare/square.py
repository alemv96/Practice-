import random

#inicializa la matriz en puros 0
def createMatrix(row,  column):
        matrix = []
        for counter in range(0 ,row):
            matrix.append([0] * column)
        return matrix

def analyseMatrix(matrix, column , row):
    diagonal, columns , rows = 0 , 0 , 0
    for countRow in range(row):
        for countColumn in range(column):
            if countRow == countColumn: diagonal += matrix[countRow][countColumn]
            columns +=  int(matrix[countRow][countColumn])
        rows += int(matrix[countRow][countColumn])

    if rows == columns and rows == diagonal and columns == diagonal: return True
    else: return False

def printMatrix(matrix , row , column):
    a=""
    for countRow in range(row):
        for countColumn in range(column):
            a += "[" + str(matrix[countRow][countColumn]) + "]" # \t si esto se coloca en una cadena significa una tabulacion
        print (a)
        a="" #reinicio a para que no se vea como un arreglo sino como una matriz

def setValues(matrix ,  column , row):
    for countRow in range(row):
        for countColumn in range(column):
            matrix[countRow][countColumn] = random.randint(0 , 5)
    return matrix
