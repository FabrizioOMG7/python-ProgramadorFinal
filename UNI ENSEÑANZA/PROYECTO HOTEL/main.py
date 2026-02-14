from datetime import date
from cliente import Cliente
from habitacion import Habitacion
from reserva import Reserva
from suite import Suite
from excepciones import HabitacionOcupadaError

# IMPORTAMOS TU NUEVA CLASE
from gestor_datos import GestorDatos 

ARCHIVO_HABITACIONES = "habitaciones.json"

def main():
    print("--- SISTEMA DE GESTIÓN HOTELERA ---\n")

    # ---------------------------------------------------------
    # 1. CARGA DE DATOS (USANDO GESTOR DE DATOS)
    # ---------------------------------------------------------
    
    # a) El Gestor trae los datos "crudos" (lista de diccionarios)
    datos_crudos = GestorDatos.cargar(ARCHIVO_HABITACIONES)
    
    lista_habitaciones = []

    if not datos_crudos:
        print("📂 No se encontró archivo. Creando datos iniciales...")
        # NOTA: Ponemos los números como STRING ("101") porque tu clase ahora lo exige.
        h101 = Habitacion("101", 2, 120, True)
        h102 = Habitacion("102", 4, 200, True)
        h103 = Suite("103", 4, 250, True, True)  # Nueva suite
        lista_habitaciones = [h101, h102, h103]
    else:
        print(f"📂 Se encontraron {len(datos_crudos)} habitaciones en el archivo.")
        # b) Convertimos los diccionarios de vuelta a OBJETOS Habitacion
        #    Usamos el método from_dict.

        for dato in datos_crudos:
            
            # 1. Leemos la etiqueta de identidad
            if dato["tipo"] == "Suite":
                # Es una Suite: Usamos el constructor de Suite (con jacuzzi)
                habitacion_obj = Suite.from_dict(dato)
            else:
                # Es normal: Usamos el constructor de Habitacion
                habitacion_obj = Habitacion.from_dict(dato)
            
            lista_habitaciones.append(habitacion_obj)
            
        print("✅ Datos convertidos exitosamente (Suites y Habitaciones detectadas).")
        
    # ---------------------------------------------------------
    # 2. LÓGICA DE NEGOCIO (Igual que antes)
    # ---------------------------------------------------------

    # Buscamos el objeto que tenga numero "101" (String)
    habitacion_101 = next((h for h in lista_habitaciones if h.numero == "101"), None)

    cliente = Cliente("Fabrizio", "f@uni.pe", True)

    if habitacion_101:
        print(f"\n--- INTENTO DE RESERVA ESTÁNDAR (Hab 101) ---")
        print(f"Estado antes de reservar: Disponible={habitacion_101.disponible}")

        try:
            # Intentamos reservar
            reserva = Reserva(
                cliente, habitacion_101, date(2025, 1, 10), date(2025, 1, 15)
            )

            print("✅ Reserva creada con éxito.")
            cliente.describir()
            habitacion_101.describir()
            print(f"Total a pagar: {reserva.calcular_total()}")

            # ---------------------------------------------------------
            # 3. GUARDAR CAMBIOS (USANDO GESTOR DE DATOS)
            # ---------------------------------------------------------
            print("\n💾 Guardando cambios en el disco...")
            
            # a) Convertimos la lista de Objetos a lista de Diccionarios
            lista_para_guardar = []
            for h in lista_habitaciones:
                lista_para_guardar.append(h.to_dict())
            
            # b) Usamos el Gestor para escribir el archivo
            GestorDatos.guardar(ARCHIVO_HABITACIONES, lista_para_guardar)
            print("✅ Cambios guardados correctamente.")

        except HabitacionOcupadaError as e:
            print(f"🛑 No se pudo reservar: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

    else:
        print("Error: No se encontró la habitación 101 en la base de datos.")

    # ---------------------------------------------------------
    # 4. DEMOSTRACIÓN DE SUITE (En memoria)
    # ---------------------------------------------------------
    print("\n--- DEMOSTRACIÓN RESERVA VIP (En memoria) ---")
    # Recuerda: Numero como string "103"
    suite = Suite("103", 4, 200, True, True) 
    
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
        reserva_fallida = Reserva(cliente,  suite, date(2025, 2, 1), date(2025, 2, 5))
    except HabitacionOcupadaError as e:
        print(f"🛑 Error detectado correctamente: {e}")
    except Exception as e:
        print(f"Ocurrió otro error: {e}")

if __name__ == "__main__":
    main()