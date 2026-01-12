import json
from habitacion import Habitacion

ARCHIVO_HABITACIONES = "habitaciones.json"


def guardar_habitaciones(lista_habitaciones):
    """Recibe una lista de OBJETOS Habitacion y los guarda en JSON."""
    lista_diccionarios = []

    # 1. Convertimos cada objeto a diccionario
    for hab in lista_habitaciones:
        lista_diccionarios.append(hab.to_dict())

    # 2. Guardamos la lista de diccionarios en el archivo
    with open(ARCHIVO_HABITACIONES, "w") as archivo:
        json.dump(lista_diccionarios, archivo, indent=4)
    print("Habitaciones guardadas correctamente.")


def cargar_habitaciones():
    """Lee el JSON y devuelve una lista de OBJETOS Habitacion."""
    try:
        with open(ARCHIVO_HABITACIONES, "r") as archivo:
            datos = json.load(archivo)  # Esto nos da una lista de diccionarios

            # Reconstruimos los objetos
            habitaciones_reconstruidas = []
            for diccionario in datos:
                habitaciones_reconstruidas.append(Habitacion.from_dict(diccionario))

            return habitaciones_reconstruidas

    except FileNotFoundError:
        # Si el archivo no existe (primera vez), devolvemos una lista vacía
        return []
