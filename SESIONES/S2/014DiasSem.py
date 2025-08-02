'''
El usuario indicará un número de día y se le imprimirá el nombre del día
'''
'''
nombre=input('Escribe tu nombre: ')
dia=int(input('Escribe el número de dia de la semana que irás a trabajar: '))

#Estructuras selectivas if --elif --else

if(dia==1):
    print(f'{nombre} Felicidades, vendrás a trabajar el día lunes')
elif(dia==2):
    print(f'{nombre} Felicidades, vendrás a trabajar el día martes')
elif(dia==3):
    print(f'{nombre} Felicidades, vendrás a trabajar el día miércoles')
elif(dia==4):
    print(f'{nombre} Felicidades, vendrás a trabajar el día jueves')
elif(dia==5):
    print(f'{nombre} Felicidades, vendrás a trabajar el día viernes')
elif(dia==6):
    print(f'{nombre} Felicidades, vendrás a trabajar el día sábado')
elif(dia==7):
    print(f'{nombre} Felicidades, vendrás a trabajar el día domingo')
else:
    print('Día no válido, intenta de nuevo...')
'''

# Creamos un diccionario con el mapeo de número de día a nombre del día
dias={
    1:'Lunes',
    2:'Martes',
    3:'Miércoles',
    4:'Jueves',
    5:'Viernes',
    6:'Sábado',
    7:'Domingo'
}
# Pedimos al usuario que ingrese un número de día
#input(): Esta función se utiliza para obtener datos de entrada del usuario a través de la consola
numero_dia=int(input('Ingrese un número de dia (1-7): '))   

# Verificamos si el número de día está dentro del rango válido
if 1 <= numero_dia <= 7:
# Imprimimos el nombre del día correspondiente al número ingresado
    print('El nombre del día es: ', dias[numero_dia])
else:
    print('Número inválido, ingrese otro número en el rango del 1-7 ')