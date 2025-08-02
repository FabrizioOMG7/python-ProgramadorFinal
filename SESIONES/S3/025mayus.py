'''Convertir a mayúsculas el texto ingresado por el usuario'''
'''
datos=input('Ingresa el texto por favor: ')
datos_mayusculas=datos.upper()
print('Los datos convertidos a mayúscula son: ', datos_mayusculas)

#Para convertir en minúsuculas 
datos_minusculas=datos.lower()
print('Los datos convertidos a minúsculas son: ', datos_minusculas) '''

datos=input('Ingresa el texto por favor: ')
opcion=int(input('Ingrese una opción: 1.Mayuscula 2.Minúscula\n')).strip() #para eliminar cualquier espacio en blanco adicional que 
#el usuario pueda haber ingresado accidentalmente.

if(opcion==1):
    datos=datos.upper()
    print('Los datos convertidos a mayúscula son: ', datos)
elif(opcion==2):
    datos=datos.lower()
    print('Los datos convertidos a minúsculas son: ', datos) 
else:
    print('Ingrese una opción válida, por favor')
