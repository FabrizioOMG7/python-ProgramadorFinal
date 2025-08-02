'''
El programa pedirá números mientras los ingresados estén entre el 0 y el 99
'''

edad=0

while True:
        edad=int(input('Escribe tu edad: '))
        if edad>0 and edad<99:
            break #Salimos porque ya tuvimos una edad válida 
        #De lo contrario seguimos en el ciclo
        print('Edad no válida, intente de nuevo por favor...')

print('Tu edad es: ', edad)