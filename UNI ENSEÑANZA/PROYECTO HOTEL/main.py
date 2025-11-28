from datetime import date
from cliente import Cliente
from habitacion import Habitacion
from reserva import Reserva

def main():
    cliente = Cliente("Fabrizio", "f@uni.pe", True)
    habitacion = Habitacion(101, 2, 120, True)
    reserva = Reserva(cliente, habitacion, date(2025,1,10), date(2025,1,15))

    print("Total", reserva.calcular_total())


if __name__ == "__main__":
    main()