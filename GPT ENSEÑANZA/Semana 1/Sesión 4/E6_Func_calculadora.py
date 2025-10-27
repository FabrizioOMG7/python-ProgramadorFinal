def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "ERROR, no se puede dividir entre 0"
    return a / b


def calculadora():
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese otro número: "))

    operacion = int(input(
        "¿Qué operación desea elegir?:\n"
        "1. Suma\n"
        "2. Resta\n"
        "3. Multiplicación\n"
        "4. División\n"
    ))

    if operacion == 1:
        resultado = sumar(a, b)
        simbolo = "+"
    elif operacion == 2:
        resultado = restar(a, b)
        simbolo = "-"
    elif operacion == 3:
        resultado = multiplicar(a, b)
        simbolo = "x"
    elif operacion == 4:
        resultado = dividir(a, b)
        simbolo = "/"
    else:
        print("Opción inválida.")
        return None, None, None, None

    return a, b, simbolo, resultado


historial = []

while True:
    a, b, simbolo, resultado = calculadora()

    if resultado is not None:
        print(f"El resultado es: {resultado}")

        # Guardar en historial
        operacion_str = f"{a} {simbolo} {b} = {resultado}"
        historial.append(operacion_str)

    continuar = input("¿Deseas hacer otra operación? (s/n): ")
    if continuar.lower() != "s":
        break

print("\nHistorial de operaciones:")
for linea in historial:
    print(linea)
