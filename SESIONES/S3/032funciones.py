'''Creamos una función para determinar si un número es par o impar'''

def es_par(num):
    if num%2==0:
        return True
    else:
        return False
    
#Aquí comienza el programa
numero=int(input('Escribe el número y determinaré si es par o impar: '))

if es_par(numero):
    print(f'El número {numero} es par')
else:
    print(f'El número {numero} es impar')