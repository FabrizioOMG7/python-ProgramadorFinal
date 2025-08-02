'''Este programa valida entradas de tipo texto'''
'''
while True:
    try:
        dato=input('Ingresa tu nombre de usuario: ')
        nombre=int(dato)
        print('Error, por favor ingrese solo texto ')
    except ValueError:
        break

print('Nombre válido: ', dato)

'''

while True:
    try:
        dato=input('Ingresa un nombre de usuario: ')
        # Quitamos los espacios al principio y al final para evitar errores por espacios innecesarios
        dato=dato.strip()
        
        # Verificamos que todos los caracteres sean letras o espacios, char toma el valor de cad caracter
        if all(char.isalpha() or char.isspace() for char in dato):
            print('El nombre de usuario es: ', dato)
            break
        else:
            print('Error al capturar, por favor ingrese solo letras.')
        
    except ValueError:
        print('Error al capturar, por favor ingrese un dato tipo texto')

#isalpha() para que solo acepte texto, isspace() para que acepte espacios
#for para recorrer cada caracter, incluyendo los espacios

'''
char = 'L' → char.isalpha() or char.isspace() es True porque 'L' es una letra.
char = 'i' → char.isalpha() or char.isspace() es True porque 'i' es una letra.
char = 'o' → char.isalpha() or char.isspace() es True porque 'o' es una letra.
... y así sucesivamente hasta que se verifiquen todos los caracteres en la cadena.
char = ' ' → char.isalpha() or char.isspace() es True porque ' ' es un espacio.
...
'''