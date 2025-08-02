'''
Comprobación de palíndromos:

Resultado esperado: Un valor booleano que indique si la cadena es un palíndromo o no.

'''

def es_palindromo(cadena):
    return cadena ==cadena[::-1]

cadena='anitalavalatina'
if es_palindromo(cadena):
    print('La cadena es un palíndromo')
else:
    print('La cadena no es un palíndromo')



'''
La Palabra Original:
La palabra original es "reconocer". Cada letra tiene una posición:

r está en la posición 0.
e está en la posición 1.
c está en la posición 2.
o está en la posición 3.
n está en la posición 4.
o está en la posición 5.
c está en la posición 6.
e está en la posición 7.
r está en la posición 8.
El Significado de [::-1]:
Ahora, vamos a entender lo que significa [::-1]:

El primer : indica dónde empezar.
El segundo : indica dónde terminar.
El -1 en medio indica el paso.
Aplicación del Slicing:

Sin nada antes del primer :, Python entiende que debe empezar desde el principio.
Sin nada después del segundo :, Python entiende que debe llegar hasta el final.
Con un -1 como paso, Python entiende que debe ir de atrás hacia adelante.
Así que, cadena[::-1] toma la palabra original y la lee desde el principio hasta el final, pero de atrás hacia adelante.

El Proceso de Inversión:

Comenzamos desde el principio de la palabra original.
Tomamos la última letra (r) y la ponemos primero en la nueva palabra.
Luego, tomamos la segunda letra (e) y la ponemos después de la r.
Después, tomamos la tercera letra (c) y la ponemos después de la e.
Luego, tomamos la cuarta letra (o) y la ponemos después de la c.
Luego, tomamos la quinta letra (n) y la ponemos después de la o.
Luego, tomamos la sexta letra (o) y la ponemos después de la n.
Luego, tomamos la séptima letra (c) y la ponemos después de la o.
Luego, tomamos la octava letra (e) y la ponemos después de la c.
Por último, tomamos la novena letra (r) y la ponemos después de la e.
¡Y ahí lo tienes! cadena[::-1] ha invertido la palabra "reconocer" para obtener "reconocer".
'''