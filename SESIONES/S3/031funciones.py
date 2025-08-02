'''El programa calculará el área de un círculo utilizando funciones'''

import math 
#Este es el método o función 
def calcular_area_circulo(radio):
    area=math.pi*radio**2
    return area

#Este es el código del programa, primero se ejecutará este código
radio=float(input('Escribe el radio del círculo y calcularé su área: '))
#Aquí llamaremos a la función 
areaCirculo=calcular_area_circulo(radio)   
print('El área del círculo es: ', round(areaCirculo,2))