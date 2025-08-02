'''Ejemplificaremos el uso de la instrucción break'''

for i in range(1,11): #Llega hasta 10, siempre se pone un número de más
    if i==6:
        print('Saliendo del sistema...')
        break #Se utiliza para salir abruptamente de un ciclo
    print('La variable i, tiene un valor de: ', i)