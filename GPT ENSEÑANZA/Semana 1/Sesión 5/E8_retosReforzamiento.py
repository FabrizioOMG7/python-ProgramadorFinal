'''
Reto fútbol:
Crea una lista con tus 5 jugadores favoritos. Luego recorre la lista con un for y cuenta cuántos tienen la letra 
"a" en su nombre. Muestra ese número al final.
'''
jugadores = ["Messi", "Neymar", "Lamine Yamal", "Lewandowski", "Palmer"]
contador2 = 0   

for jugador in jugadores:
    if "a" in jugador.lower():
        contador2+=1
        
    contador = 0
    for letra in jugador:
        if letra.lower() == "a":
            contador +=1
            
    print(f"El jugador {jugador} tiene {contador} letras")
print(f"{contador2} jugadores tienen la letra 'a' en su nombre" )
