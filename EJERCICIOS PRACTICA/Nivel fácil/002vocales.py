'''Contador de vocales: Crea un programa que cuente el número de vocales en una cadena de texto dada.

'''
cadena=input('Ingrese un texto cualquiera: ')
vocales='aeiouAEIOU'
cantidad=0

for letra in cadena:
    if letra in vocales:
        cantidad+=1

print(f'La cantidad de vocales es: {cantidad}')


