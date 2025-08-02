'''
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''

#Operadores aritméticos
a=int(input("Ingrese un número a sumar: "))
b=int(input("Ingrese otro número a sumar: "))
resultado=a+b
print("El resultado es: " , resultado)

print(f"suma: 10 + 3 = {10+3}")

#Operadores de comparación
print(f"Igualdad: 10==3 es {10==3} ")
print(f"Desigualdad: 10!=3 es {10!=3} ")
print(f"Mayor que: 10 > 3 es {10>3}")
print(f"Menor que: 10 < 3 es {10<3}")
print(f"Mayor o igual que: 10 >= 3 es {10>=3}")
print(f"Menor o igual que: 10 <= 3 es {10<=3}")

#Operadores lógicos