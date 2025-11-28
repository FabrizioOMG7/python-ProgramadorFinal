# Definimos la clase habitación
class Habitacion:
    def __init__(self, numero, capacidad, precio_por_noche, disponible):

        # Dentro de la instancia colocamos las restricciones
        if not isinstance(capacidad, int):
            raise ValueError("La capacidad debe ser un valor entero")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser un número positivo")
        if not isinstance(precio_por_noche, (int, float)):
            raise ValueError("El precio debe ser un valor numérico")
        if precio_por_noche <= 0:
            raise ValueError("El precio por noche debe ser un valor positivo")
        if not isinstance(disponible, bool):
            raise ValueError("El estado disponible debe ser booleano (True o False)")

        self.numero = numero
        self.capacidad = capacidad
        self.precio_por_noche = precio_por_noche
        self.disponible = disponible

    # metodos:
    def describir(self):
        print(
            f"Habitación {self.numero} - Capacidad: {self.capacidad} personas - Precio: {self.precio_por_noche} -  Disponible: {self.disponible}"
        )
