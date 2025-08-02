'''Ejemplificaremos el uso de continue
El programa solamente imprimirá el valor de la variable cuando esta sea impar
'''

for i in range(1,11):
    if i%2==0:
        print('Impresión omitida por ser un número par...')
        continue #omite la impresión del número y vuelve a realizar el recorrido con el for
    print(f'La variable i vale: {i}')