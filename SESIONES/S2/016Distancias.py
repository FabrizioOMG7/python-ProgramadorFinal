'''Convertiremos de metros a kilómetros y a centímetros
    según lo solicite el usuario
'''

distancia=float(input('Escribe la cantidad en metros: '))
opcion=input('\n ¿A qué unidad de medida lo quieres convertir?: '
                '\na. Convertir a kilómetros'
                '\nb. Convertir a centímetros\n')

if opcion=='a':
    total=distancia/1000
    print('La cantidad convertida en kilometros es: ', total)
elif opcion=='b':
    total=distancia*100
    print(f'La cantidad convertida en centimetros es: {total}')
else:
    print('La opción no es valida...')