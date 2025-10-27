texto = input("Ingrese una cadena de texto: ")

vocales = ["a","e","i","o","u"]
vocales_encontradas = []
contador = 0

for letras in texto:
    if letras in vocales:
        contador +=1
        vocales_encontradas.append(letras)
        

print(f"La cantidad de vocales encontradas son: {contador}")

print(f"Las vocales encontradas son: {vocales_encontradas}")