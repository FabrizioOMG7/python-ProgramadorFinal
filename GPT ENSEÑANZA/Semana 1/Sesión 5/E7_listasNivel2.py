
'''
### 1. 🎮 *FIFA Manager*

Crea una lista con 5 jugadores famosos. Agrega un nuevo fichaje con `.append()`, 
elimina un jugador con `.remove()` y muestra la lista actualizada.
'''
jugadores = ["Lamine Yamal", "Rapinha", "Lewandowski", "Pedri", "Gavi"]

jugadores.append("Rashford")
jugadores.remove("Pedri")

print("Lista de jugadores: ", jugadores)

'''
### 2. 🎲 *Top 5 Juegos Favoritos*

Haz que el usuario ingrese 5 juegos. Luego:

- Inserta tu juego favorito en la posición 2.
- Elimina el último con `.pop()`.
    - Muestra la lista al revés.
'''
juegos=[]

for i in range (5):
    juego = input(f"Ingrese el nombre del juego #{i+1}: ")
    juegos.append(juego)

juegos.insert(1,"Fornite")


juegos.pop(-1)
print("Tus juegos favoritos son: ", juegos)
juegos.reverse()

print("Los juegos al revés son: ", juegos)

#JUEGOS CON MÁS DE 7 LETRAS EN SU PALABRA
for juego in juegos:
    if len(juego) > 7:
        print("Los juegos con más de 7 letras son: ", juego)

for juego in juegos:
    contador = 0
    for letra in juego:
        if letra == "a" :
            contador +=1
    print(f"El juego {juego} tiene {contador} letras 'a'  " )

#Convirtiendo los nombres de los juegos a mayúscula

juegos_mayuscula = []

for juego in juegos:
    juegos_mayuscula.append(juego.upper())
print("Juegos en mayúsculas: " , juegos_mayuscula)



