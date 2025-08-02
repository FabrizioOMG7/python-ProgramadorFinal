'''
El programa pedirá una cantidad en pesos mexicanos y mostrará un menú de opciones
para convertir a dólares o soles peruanos
'''
pesos=int(input('Escribe la cantidad en pesos mexicanos: '))
opcion=int(input('\n ¿A cúal moneda deseas convertir?: '
                    '\n1. Dólares $16' 
                    '\n2. Sol peruano S/4\n' ))

mensaje1='La cantidad convertida en dólares es: '
mensaje2='La cantidad convertida en soles peruanos es: '
ancho=80

if(opcion==1):
    total=pesos/16
    mensaje1=mensaje1.center(ancho)
    print(mensaje1,round(total,2))
elif(opcion==2):
    total=pesos/4
    mensaje2=mensaje2.center(ancho) 
    print(mensaje2,round(total,2))
else:
    print('Esa opción no existe...')