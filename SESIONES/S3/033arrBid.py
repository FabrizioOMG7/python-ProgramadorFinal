'''El programa manipula un arreglo bidimensional, también llamado matriz
    o listas de listas
'''

#Crearemos una matriz
matriz=[[1,2,3], 
        [4,5,6],
        [7,8,9]]

#Como accedemos a un determinado elemento de la matriz
elemento=matriz[1][2]
print('El elemento que está en la fila 1, columna 2 es: ', elemento)

print('Ahora recorreremos toda la estructura: ')
for fila in matriz: 
    for elemento in fila:
        print(elemento,end=' ')
    print()