#Determina si una persona puede o no votar, evaluando su edad
nombre=input('Escribe tu nombre: ')
edad=int(input('Ingrese tu edad: '))

if(edad>=18) and(edad<=60): #Estructura selectiva
    print(nombre,', Estás habilitado para votar')
else:
    print(nombre,', No estás habilitado para votar')