try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("Error, no se ha ingresado un número válido")
else:
    if numero % 2 == 0:
        print(f"El número {numero} es par")
    
    else:
        print(f"El número {numero} es impar")






