'''Este programa valida para que solo se introduzca datos numéricos '''

while True:
    try: #Intenta hacer que:
        datos=input('Por favor ingresa tu edad: ')
        edad=int(datos)
        if(edad<0) or (edad>99): #Se utiliza or porque solo se tiene que cunplir una de las 2 condiciones, las dos no, ya que es imposible
            print('Edad no válida')
        else:
            break
    except ValueError: #Si el tipo de dato no es el apropiado
        print('Error al capturar, por favor ingresa un dato numérico ')
    
print('Tu edad es: ', edad)