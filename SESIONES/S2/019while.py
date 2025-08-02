'''El programa contiene un número secreto que el usuario debe adivinar
    Tendrá 3 oportinidades
'''

import random

numero_secreto=random.randint(1,10) #Para que se genere un número aleatorio
adivinado=False
intentos=0
quedan=3

print('Solo tienes 3 intentos para adivinar. ')
while not(adivinado) and (intentos<3): #Mientras adivinado no sea verdadero y los intentos sea menor a 3...
    dato=int(input('Adivina el número(Es menor que 10): '))
    if(dato==numero_secreto):
        #Si adivina el número 
        print('Felicitaciones, haz adivinado el número secreto...')
        adivinado=True
    else:
        #Si no lo adivinó
        intentos+=1 
        if(intentos==3): #Si intentos ya llegó a 3
            print('Juego terminado...')
        else: #En caso no se llegue a 3 intentos
            print('Por favor, inténtalo de nuevo...')
            quedan-=1
            print(f'te quedan {quedan} intentos')



'''
numero_secreto=9
adivinado=False
intentos=0
quedan=3

print('Solo tienes 3 intentos para adivinar. ')
while not(adivinado) and (intentos<3): #Mientras adivinado no sea verdadero y los intentos sea menor a 3...
    dato=int(input('Adivina el número(Es menor que 10): '))
    if(dato==numero_secreto):
        #Si adivina el número 
        print('Felicitaciones, haz adivinado el número secreto...')
        adivinado=True
    else:
        #Si no lo adivinó
        intentos+=1 
        if(intentos==3): #Si intentos ya llegó a 3
            print('Juego terminado...')
        else: #En caso no se llegue a 3 intentos
            print('Por favor, inténtalo de nuevo...')
            quedan-=1
            print(f'te quedan {quedan} intentos') '''
