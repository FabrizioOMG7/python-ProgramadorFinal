'''El programa evaluará la estatura del usuario y 
1.Si la estatura es menor que 160 cm imprimirá: Eres un pitufo
2.Si la estatura está entre 160 y 175 cm imprimirá: Eres de estatura mediana
3.Si la estatura es mayor a 175 cm imprimirá: Eres alto
'''
nombre=input('Escribe tu nombre: ')
estatura=int(input('Escribe tu estatura en centimetros: '))
sexo=input('Escribe tu sexo:(H/M)') 

if(estatura<160):
    if(sexo=='h'):
        print(f'{nombre} Eres un pitufo con {estatura} cm')  #if anidados (if dentro de un if)
    else:
        print(f'{nombre} Eres una pitufa con {estatura} cm')

elif(estatura>=160 and estatura<=175):
    if(sexo=='h'):
        print(f'{nombre} Eres de estatura mediana con {estatura} cm')
    else:
        print(f'{nombre} Eres de estatura mediana con {estatura} cm')
else:
    if(sexo=='h'):
        print(f'{nombre} Eres alto con {estatura} cm')
    else:
        print(f'{nombre} Eres alta con {estatura} cm')

'''También se pueden utilizar if por separado
    if:
    if:
    if:
'''

'''
El f es para colocar variables e imprimirlos como texto, solo los metemos entre llaves, ya no es necesario usar " , "
'''