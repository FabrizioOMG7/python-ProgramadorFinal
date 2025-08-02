'''
El programa pedirá números para promediarlos
El while true se ejecuta por lo menos 1 vez
'''

contador=0
suma=0
numero=0

while True: #do --while (mientras la verdad sea verdad)
    numero=float(input('Escribe un número para sumarlo (Ingresa 0 para salir): '))
    if(numero==0): #Si el número es cero, se saldrá del ciclo con la instrucción break
        break
    #Si no es cero
    suma+=numero
    contador+=1
#Una vez que se haya salido del ciclo
if(contador>0):
    promedio=suma/contador
    print(f'La suma de los números es: {suma} ')
    print(f'El total de los números introducidos es: {contador} ')
    print(f'El promedio de los números ingresados es: {promedio}')
else:
    print('No se ingresaron números válidos...')
    