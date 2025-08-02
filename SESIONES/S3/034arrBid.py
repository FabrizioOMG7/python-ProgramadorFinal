#Crearemos una lista de listas que llenaremos desde el teclado

filas=3
columnas=3
matriz=[[9]*columnas for _ in range (filas)]

for i in range (filas):
    for j in range (columnas):
        dato=input ('Ingresa el dato para la posicion ({},{})' .format(i,j))
        matriz[i][j]=dato

print('\n Los datos de la matriz son: ')
for fila in matriz:
    print(fila)

#Imprimeremos la diagonal principal
print('\n Imprimiremos la diagonal principal ')
for i in range(3):
    for j in range(3):
        if i==j:
            print(matriz[i][j])