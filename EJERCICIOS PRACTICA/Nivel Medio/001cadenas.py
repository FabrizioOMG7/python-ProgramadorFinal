'''
Inversión de cadenas:

Resultado esperado: La cadena de texto invertida.
'''
cadena=input('Ingrese una texto: ')
cadena_invertida='' #Aquí se almacena el código de la cadena invertida, al comienzo está vacío

for caracter in cadena:
    cadena_invertida = caracter + cadena_invertida

print(f'La cadena invertida es: {cadena_invertida}')

'''
Iteraciones del bucle: ejemplo messi

Primer carácter: m
cadena_invertida = 'm' + ''  # 'm'
cadena_invertida ahora es "m".

Segundo carácter: e
cadena_invertida = 'e' + 'm'  # 'em'
cadena_invertida ahora es "em".

Tercer carácter: s
cadena_invertida = 's' + 'em'  # 'sem'
cadena_invertida ahora es "sem".

Cuarto carácter: s
cadena_invertida = 's' + 'sem'  # 'ssem'
cadena_invertida ahora es "ssem".

Quinto carácter: i
cadena_invertida = 'i' + 'ssem'  # 'issem'
cadena_invertida ahora es "issem".
'''