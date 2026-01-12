import unittest
from datetime import date
from cliente import Cliente
from habitacion import Habitacion
from reserva import Reserva
from excepciones import HabitacionOcupadaError

class TestSistemaHotel(unittest.TestCase):

    def setUp(self):
        """Esto se ejecuta ANTES de cada prueba para preparar el terreno"""
        self.cliente = Cliente("Tester", "test@uni.pe", True)
        self.habitacion = Habitacion(999, 2, 100, True)

    def test_reserva_exitosa_cambia_disponibilidad(self):
        """Prueba 1: Si reservo, la habitación debe quedar ocupada (False)"""
        #Actuar
        Reserva(self.cliente, self.habitacion, date(2025,1,1), date(2025,1,5))

        #Verificar (Assert)
        #Espero que la habitación disponible sea False"
        self.assertFalse(self.habitacion.disponible)

    def test_reserva_habitacion_ocupada_lanza_error(self):
        """Prueba 2: Si la habitación ya está ocupada, debe lanzar TU error personalizado"""
        # 1. Ocupamos la habitación manualmente primero
        self.habitacion.disponible = False

        # 2. Intentamos reservar de nuevo y esperamos que EXPLOTE controladamente
        # "Espero que al hacer esto, se lance HabitacionOcupadaError"
        with self.assertRaises(HabitacionOcupadaError):
            Reserva(self.cliente, self.habitacion, date(2025,2,1), date(2025,2,5))

if __name__ == '__main__':
    unittest.main()
