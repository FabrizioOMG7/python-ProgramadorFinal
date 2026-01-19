#Esta librería nos ayudará a mantener los datos guardados
import json

class GestorDatos:

    @staticmethod
    def guardar(nombre_archivo: str, datos: list):
        """
        Guarda una lista de diccionarios en un archivo JSON.
        :param nombre_archivo: Ruta del archivo (ej: "clientes.json")
        :param datos: Lista de diccionarios (ya convertidos con to_dict)
        """
        # 'w' significa Write (Escritura). Si el archivo no existe, lo crea.
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)

    @staticmethod
    def cargar(nombre_archivo: str):
        try:
            with open(nombre_archivo, 'r') as archivo:
                return json.load(archivo)
        except FileNotFoundError:
            return []