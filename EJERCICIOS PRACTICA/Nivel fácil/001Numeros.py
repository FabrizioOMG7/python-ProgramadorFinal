'''
Suma de números pares e impares: Escribe un programa que sume todos los números
pares e impares por separado dentro de un rango dado.
'''
suma_par=0
suma_impar=0

for i in range(1,11):
    if i%2==0:
        suma_par+=i
        
    elif i%2!=0:
        suma_impar+=i

print(f'La suma de los números pares es: {suma_par}')
print(f'La suma de los números impares es: {suma_impar}')

