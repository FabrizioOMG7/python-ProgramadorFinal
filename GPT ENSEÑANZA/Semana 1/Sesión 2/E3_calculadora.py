num1 = float(input(f"Ingrese un número: \n"))
num2 = float(input(f"Ingrese un segundo número: \n"))

operacion = input(f"¿Qué operación desea elegir?: 1.Suma 2.Resta 3.Multiplicación 4.División\n")

if operacion == "1":
    resultado =num1 + num2

elif operacion == "2":
    resultado= num1 - num2

elif operacion == "3":
    resultado = num1 * num2

elif operacion =="4":
    if num2 == 0:
        print("Error, esta división no se puede realizar")
    else:
        resultado = num1 /num2
else: 
    print("Operación no válida")


print(f"El resultado de la operación es: {resultado}")

