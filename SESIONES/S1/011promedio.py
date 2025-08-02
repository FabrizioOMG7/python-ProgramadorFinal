#El programa calcula y muestra el promedio de calificaciones de un alumno
print('Calcularesmos el promedio de 3 calif de un alumno\n')
nombre=input('Escribe tu nombre alumno: ')
mat=float(input('Escribe tu calif de matemática: '))
fis=float(input('Escribe tu calificación de fisica: '))
quim=float(input('Escribe tu calificación de química: '))

prom=(mat+fis+quim)/3

print(nombre, 'Tu promedio es: ', prom)

#Ahora indicaremos si el alumno está aprobado o reprobado

if(prom<12):
    print(nombre, 'Estás reprobado, con el promedio', prom)
else: 
    print(nombre, 'Estás aprobado, con el promedio', prom)