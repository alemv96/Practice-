import math
#en este modulo se colocaran los metodos para hallar ecuaciones de primer grado, segundo grado etc...
def secondGradeEquation(firstCoheficent , secondCoheficent , thirdCoheficent):
    firstResult = (-secondCoheficent + math.sqrt(secondCoheficent** - 4*firstCoheficent*thirdCoheficent))/2*firstCoheficent
    secondResult = (-secondCoheficent - math.sqrt(secondCoheficent** - 4*firstCoheficent*thirdCoheficent))/2*firstCoheficent
    print("x1 = " , firstResult)
    print("x2 = " , secondResult)
