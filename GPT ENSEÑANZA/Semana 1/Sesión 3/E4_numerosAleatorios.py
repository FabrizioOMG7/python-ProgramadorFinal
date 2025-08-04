'''Juego: Adivina el número (versión simple)
🔹 Parte 1: Preparación
Primero, el programa necesita elegir un número secreto. En Python, para generar un número aleatorio usamos el módulo random.'''

import random

numero_aleatorio = random.randint(1,10)

num = int(input("Ingrese un número: \n"))
intentos = 1

while num != numero_aleatorio:
    print("--FALLASTE!!--\n")
    intentos+=1
    num = int(input("Ingrese otro número: \n"))
    
print(f"Felicidades, el número {num} coincide con el número aleatorio {numero_aleatorio}")
print(f"Lograste realizarlo en {intentos} intentos")


'''
if num == numero_aleatorio:
    print (f"El número {num} coincide con el número aleatorio generado({numero_aleatorio})")
else:
    print(f"El número {num} no coincide con el número aleatorio generado ({numero_aleatorio})")'''
    
