#Importamos DatosInvalidosError del archivo excepciones
from excepciones import DatosError, DatosInvalidosError, TipoDatoError

# Definimos la clase habitación
class Habitacion:
    def __init__(self, numero:str, capacidad:int, precio_por_noche:float, disponible:bool = True):

        # Dentro de la instancia colocamos las restricciones
        if not isinstance(capacidad, int):
            raise TipoDatoError("La capacidad debe ser un valor entero")
        if capacidad <= 0:
            raise DatosInvalidosError("La capacidad debe ser un número positivo")
        if not isinstance(precio_por_noche, (int, float)):          
            raise TipoDatoError("El precio debe ser un valor numérico")
        if precio_por_noche <= 0:
            raise DatosInvalidosError("El precio por noche debe ser un valor positivo")
        if not isinstance(disponible, bool):
            raise TipoDatoError("El estado disponible debe ser booleano (True o False)")
        if not isinstance(numero, str):
            raise TipoDatoError("El número de la habitación no debe estar vacío")
        self.numero = numero
        self.capacidad = capacidad
        self.precio_por_noche = precio_por_noche
        self._disponible = disponible

# 1. EL GETTER (Para leer: habitacion.disponible)
    @property
    def disponible(self):
        return self._disponible
    
# 2. EL SETTER (Para escribir: habitacion.disponible = False)
    @disponible.setter
    def disponible(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El estado disponible debe ser booleano")
        
        self._disponible = valor

        
    # metodos:
    def describir(self):
        print(
            f"Habitación {self.numero} - Capacidad: {self.capacidad} personas - Precio: {self.precio_por_noche} -  Disponible: {self.disponible}"
        )

    def pago_extra(self):
        return 0

    # --- NUEVOS MÉTODOS PARA PERSISTENCIA ---

    def to_dict(self):
        """Convierte el objeto en un diccionario simple."""
        return {
            "numero": self.numero,
            "capacidad": self.capacidad,
            "precio_por_noche": self.precio_por_noche,
            "disponible": self.disponible # Usamos la propiedad pública
        }

    @classmethod
    def from_dict(cls, data):
        """Crea una instancia de Habitacion desde un diccionario."""
        # data es el diccionario que cargamos del JSON
        return cls(
            numero = data["numero"],
            capacidad = data["capacidad"],
            precio_por_noche = data["precio_por_noche"],
            disponible = data["disponible"]
        )







'''
# A esto se le llama encapsulación
    def esta_disponible(self):
        if self.__disponible:
            return True
        else:
            return False 

#Cuándo alguien necesite ocupar una habitación solo se llama a este método   

    def ocupar(self):
        self.__disponible = False
'''
