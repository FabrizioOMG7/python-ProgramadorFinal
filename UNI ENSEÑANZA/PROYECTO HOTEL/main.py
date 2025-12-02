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

    print("Total", reserva.calcular_total())
    print("Total VIP:", reserva_vip.calcular_total())


if __name__ == "__main__":
    main()  