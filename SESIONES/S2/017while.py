'''Simularemos el conteo regresivo del despegue de un cohete '''
import time #Librería para usar el tiempo

contador=10

print('Inicia el conteo regresivo...')
while contador>0: #Puede que nunca se ejecute
    print(contador)
    time.sleep(1) #1 segundo lo mandamos a dormir con sleep, es para que demore "x" segundos para mostrar el resultado
    contador-=1 #contador=contador-1
print('El cohete ha despegado con éxito...')