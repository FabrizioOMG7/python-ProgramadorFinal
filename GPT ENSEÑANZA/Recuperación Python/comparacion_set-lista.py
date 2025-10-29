import time

# Lista y set con las mismas vocales
vocales_lista = ["a", "e", "i", "o", "u"]
vocales_set = {"a", "e", "i", "o", "u"}

# Vamos a buscar muchas veces una letra
pruebas = 1_000_000
letra = "u"

# Medir tiempo con lista
inicio = time.time()
for _ in range(pruebas):
    letra in vocales_lista
print("Tiempo con lista:", time.time() - inicio)

# Medir tiempo con set
inicio = time.time()
for _ in range(pruebas):
    letra in vocales_set
print("Tiempo con set:", time.time() - inicio)
