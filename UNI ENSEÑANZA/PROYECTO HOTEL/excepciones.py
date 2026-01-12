class HotelError(Exception):
    """Clase base (padre) para todos los errores de nuestro sistema hotelero."""
    pass

# 1. Errores de Validación (Sanitización de Datos)

class DatosError(HotelError):
    """Clase padre para errores de formato o tipos de datos incorrectos."""
    pass

class DatosInvalidosError(DatosError):
    """Se lanza cuando el formato del dato está mal (ej: email sin @, nombre vacío).""" 
    pass

class TipoDatoError(DatosError):
    """Se lanza cuando el tipo de dato no es el esperado (ej: str en vez de int)."""
    pass

# 2. Errores de Lógica de Negocio (Reglas del Hotel)

class OperacionError(HotelError):
    """Clase padre para operaciones que no se pueden realizar por el estado del sistema."""
    pass

class HabitacionOcupadaError(OperacionError):
    """ Se lanza cuando intentas reservar una habitación que ya está ocupada."""
    pass

class ClienteInactivoError(OperacionError):
    """Se lanza cuando el cliente no está activo y quiere reservar."""
    pass

class FechasInvalidasError(OperacionError):
    """(TUYO) Se lanza cuando la fecha fin es menor a la fecha de inicio."""
    pass

