from datetime import date
from habitacion import Habitacion
from cliente import Cliente


# Definimos la clase reserva
class Reserva:
    # Instanciamos para agregar las clases (composición)
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):

        # Validaciones
        if not isinstance(cliente, Cliente):
            raise TypeError("Se espera un objeto de la clase cliente")
        if not isinstance(habitacion, Habitacion):
            raise TypeError("Se espera un objeto de la clase habitacion")
        if not habitacion.disponible:
            raise ValueError("No hay habitaciones disponibles")
        if not cliente.esta_activo():
            raise ValueError("El cliente no está activo")
        if not isinstance(fecha_inicio, date):
            raise ValueError("La fecha de inicio debe ser de tipo de dato Date ")
        if not isinstance(fecha_fin, date):
            raise ValueError("La fecha fin debe ser de tipo de dato Date")
        if fecha_inicio >= fecha_fin:
            raise ValueError("La fecha fin debe ser mayor a la fecha de inicio")

        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.habitacion.disponible = False

        # Método

    def calcular_total(self):

        dias = (self.fecha_fin - self.fecha_inicio).days

        return (dias * self.habitacion.precio_por_noche) + self.habitacion.pago_extra()
