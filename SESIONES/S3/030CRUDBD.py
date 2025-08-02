
# pip install mysql-connector-python


import os
import time
import mysql.connector

#Conectar a la base de datos
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='pruebaperu'
)

#Un cursor se utiliza para ejecutar comandos SQL en la base de datos
mycursor=mydb.cursor()

#Creamos el menú
while True:
    print('---Menú del sistema---'
        '\n1.Insertar un registro'
        '\n2.Eliminar un registro'
        '\n3.Buscar un registro'
        '\n4.Sobreescribir un registro'
        '\n5.Mostrar el contenido de la base de datos'
        '\n6.Salir del sistema')
    opcion=int(input('Elige una opción: '))
    if opcion==1: #Create (insertar)
        dato=input('Ingresa el dato a insertar: ')
        sql='INSERT INTO datos (dato) VALUES (%s)'
        val=(dato,) #guardar el dato 
        mycursor.execute(sql,val) #Ejecuta la instrucción sql y guardalo el valor de val
        mydb.commit() #Para que se guarden los cambios en la bd
        print(mycursor.rowcount,'Registros insertados') #Cuenta las filas que fueron afectadas por el objeto mycursor
        time.sleep(2)
        os.system('cls') #Limpiar pantalla

    elif opcion==2: #Delete (eliminar)
        dato=input('Ingresa el dato a eliminar: ')
        sql='DELETE FROM datos WHERE dato=%s'
        val=(dato,)#lo que va a borrar esta en la variable dato
        mycursor.execute(sql,val) #Lo que va a ejecutar, va a afectar a los datos de la variable val
        mydb.commit() #Para que se guarden los cambios en la bd
        print(mycursor.rowcount,'Registros eliminados')
        time.sleep(2)
        os.system('cls')

    elif opcion==3: #Read(leer)
        dato=input('Ingrese el dato a buscar: ')
        sql='SELECT * FROM datos WHERE dato=%s'
        val=(dato,)
        mycursor.execute(sql,val)
        myresult=mycursor.fetchall() #Para ver todos los datos obtenidos en mycursor
        if myresult:
            print('El dato está en la tabla. ')
        else:
            print('El dato no existe en la tabla')
            time.sleep(2)
            os.system('cls')
    
    elif opcion==4: #Update (actualizar)
        datoAnterior=input('Ingresa el dato a sobreescribir: ')
        datoNuevo=input('Ingrese el dato nuevo: ')
        sql='UPDATE datos SET dato=%s WHERE dato=%s'
        val=(datoNuevo,datoAnterior)
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount,'Registros actualizados')
        time.sleep(2)
        os.system('cls')
    elif opcion==5: #Mostrar contenido bd
        mycursor.execute('SELECT * FROM datos')
        myresult=mycursor.fetchall() #mycursor es para ejecutar comandos sql y fetchall recupera todos los resultados
        print('Contenido de la tabla: ') 
        for x in myresult: #se imprime el contenido de la tabla fila por fila.
            print(x)
        time.sleep(4)
        os.system('cls')
    elif opcion==6: #Salir del sistema
        respuesta=input('Estás seguro?  (s/n): ')
        if respuesta.upper()=='S':
            print('Saliendo del sistema...')
            time.sleep(2)
            os.system('cls')
            break
        time.sleep(2)
        os.system('cls')
    else: #En cualquier otro caso
        print('Opción no válida, intenta de nuevo...')
        time.sleep(2)
        os.system('cls')

'''
%s se utiliza como marcador de posición para el valor que se va a 
insertar en la columna dato de la tabla datos. La variable val es una tupla que 
contiene el valor real que se desea insertar. Al llamar a mycursor.execute(sql, val),
el valor contenido en val se sustituirá en lugar del marcador %s en la consulta 
SQL antes de ejecutarla.
'''

'''
fetchall() es utilizado para recuperar todos los resultados de una consulta ejecutada 
con un cursor en una base de datos en Python.
'''