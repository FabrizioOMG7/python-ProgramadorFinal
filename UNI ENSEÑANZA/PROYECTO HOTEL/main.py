from datetime import date
from cliente import Cliente
from habitacion import Habitacion
from reserva import Reserva
from archivos import guardar_habitaciones, cargar_habitaciones
from suite import Suite
from excepciones import HabitacionOcupadaError


def main():
    print("--- SISTEMA DE GESTIÓN HOTELERA ---\n")

    # 1. CARGA DE DATOS (PERSISTENCIA)
    lista_habitaciones = cargar_habitaciones()

    # Si no hay archivo, creamos las habitaciones por defecto
    if not lista_habitaciones:
        print("📂 No se encontró archivo. Creando datos iniciales...")
        h101 = Habitacion(101, 2, 120, True)
        h102 = Habitacion(102, 4, 200, True)
        lista_habitaciones = [h101, h102]
    else:
        print("📂 Datos cargados del archivo exitosamente.")

    # 2. SELECCIONAMOS LA HABITACIÓN 101 DE LA LISTA (NO creamos una nueva)
    # Buscamos el objeto que tenga numero 101
    habitacion_101 = next((h for h in lista_habitaciones if h.numero == 101), None)

    cliente = Cliente("Fabrizio", "f@uni.pe", True)

    if habitacion_101:
        print(f"\n--- INTENTO DE RESERVA ESTÁNDAR (Hab 101) ---")
        print(f"Estado antes de reservar: Disponible={habitacion_101.disponible}")

        try:
            # Intentamos crear la reserva USANDO EL OBJETO DE LA LISTA
            # Si ya estaba ocupada (del archivo), esto lanzará el error aquí mismo.
            reserva = Reserva(
                cliente, habitacion_101, date(2025, 1, 10), date(2025, 1, 15)
            )

            # Si logramos pasar aquí, es que se reservó con éxito
            print("✅ Reserva creada con éxito.")
            cliente.describir()
            habitacion_101.describir()
            print(f"Total a pagar: {reserva.calcular_total()}")

            # 3. GUARDAMOS LOS CAMBIOS
            # Como modificamos habitacion_101 (que está dentro de la lista), al guardar la lista, se guarda el cambio.
            guardar_habitaciones(lista_habitaciones)

        except HabitacionOcupadaError as e:
            print(f"🛑 No se pudo reservar: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    else:
        print("Error: No se encontró la habitación 101 en la base de datos.")

    # 4. DEMOSTRACIÓN DE SUITE (Esto va aparte porque no estamos guardando suites todavía)
    print("\n--- DEMOSTRACIÓN RESERVA VIP (En memoria) ---")
    suite = Suite(103, 4, 200, True, True)
    try:
        reserva_vip = Reserva(cliente, suite, date(2025, 1, 5), date(2025, 1, 10))
        cliente.describir()
        suite.describir()
        print(f"Total a pagar: {reserva_vip.calcular_total()}")
    except Exception as e:
        print(f"Error en VIP: {e}")

    # 5. PRUEBA DE ERROR FORZADO
    print("\n--- PRUEBA DE ERROR CONTROLADO ---")
    try:
        # Intentamos reservar la misma suite ocupada arriba
        reserva_fallida = Reserva(cliente, suite, date(2025, 2, 1), date(2025, 2, 5))
    except HabitacionOcupadaError as e:
        print(f"🛑 Error detectado correctamente: {e}")
    except Exception as e:
        print(f"Ocurrió otro error: {e}")


if __name__ == "__main__":
    main()
