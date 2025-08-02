'''EL programa pedirá números y los irá sumando en una variable que
técnicamente se conoce como acumulador
'''

suma=0 #Al comienzo suma no debe tener ningun valor
numero=1 #Se le pone un valor diferente al 0 para que entre al while

while numero!=0: #mientras...
    numero=int(input('Ingresa un número para sumarlo, (ingresa 0 para salir): '))
    suma+=numero #suma=suma+numero

print('La suma de los números introducidos es: ', suma)