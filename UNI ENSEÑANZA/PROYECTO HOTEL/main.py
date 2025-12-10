from datetime import date
from cliente import Cliente
from habitacion import Habitacion
from reserva import Reserva

from suite import Suite

def main():
    cliente = Cliente("Fabrizio", "f@uni.pe", True)
    habitacion = Habitacion(101, 2, 120, True)
    reserva = Reserva(cliente, habitacion, date(2025,1,10), date(2025,1,15))

    suite = Suite(103, 4, 200, True, True)
    suite.describir()

    reserva_vip = Reserva(cliente, suite,date(2025,1,5), date(2025,1,10) )

    # BLOQUE 1: La Reserva Normal
    print("\n--- RESERVA ESTÁNDAR ---")
    cliente.describir()
    habitacion.describir()
    print(f"Total a pagar: {reserva.calcular_total()}")

    # BLOQUE 2: La Reserva VIP
    print("\n--- RESERVA VIP ---")
    cliente.describir()
    suite.describir()
    print(f"Total a pagar: {reserva_vip.calcular_total()}")

if __name__ == "__main__":
    main()