'''
Calculadora de factorial:
Resultado esperado: El factorial del número dado.
'''
numero=int(input('Ingrese un número: '))

def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
print(f'El factorial de {numero} es {factorial(numero)}')