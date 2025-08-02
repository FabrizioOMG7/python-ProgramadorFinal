

print('***Bienvenido a mi calculadora básica***')
print ('_______________________________________')
a = int(input("ingrese el primer numero: "))
b = int(input("ingrese el segundo numero: "))
print('Elige una opción: ' )
print('1.Suma')
print('2.Resta')
print('3.Multiplicación')
print('División')


opcion = int(input("Ingrese una oopcion del menu y dale enter: "))

match opcion:
    case 1:
        print("Usted ha elegido la opcion de summa.")
        resultado=a+b
    case 2:
        print("Usted ha elegido la opcion de resta.")
        resultado=a-b
    case 3:
        print("Usted ha elegido la opcion de multiplicacion.")
        resultado=a*b
    case 4:
        print("Usted ha elegido la opcion de division.")
        resultado=a/b
    case _:
        print("Opcion invalida. Ejecute de nuevo el programa")


print(f'El resultado de la operación elegida es: {resultado}')