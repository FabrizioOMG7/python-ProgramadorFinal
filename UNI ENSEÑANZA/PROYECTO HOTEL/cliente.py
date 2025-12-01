# Definimos la clase cliente
class Cliente:
    def __init__(self, nombre, email, activo):

        # Restricciones de la clase cliente
        if not isinstance(nombre, str):
            raise ValueError("El nombre deben ser caracteres de texto (String)")
        if len(nombre.strip()) <= 0:
            raise ValueError("El nombre del cliente no puede estar vacío")
        if not isinstance(email, str):
            raise ValueError("El email deben ser string")
        if "@" not in email:
            raise ValueError("El email debe tener un @ ")
        if not isinstance(activo, bool):
            raise ValueError("El estado activo debe ser booleano (True o False)")

        self.nombre = nombre
        self.email = email
        self.__activo = activo

    # metodos:
    def desactivar(self):
        self.__activo = False

    def activar(self):
        self.__activo = True

    def esta_activo(self):
        if self.__activo:
            return True
        else: 
            return False
