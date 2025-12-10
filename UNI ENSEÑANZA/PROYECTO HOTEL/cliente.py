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

        self.nombre = nombre
        self.email = email
        self.activo = activo

    def describir(self):
        return f"Cliente: {self.nombre} - Email: {self.email} - Activo: {self._activo}"

    # metodos:
    def desactivar(self):
        self._activo = False

    def activar(self):
        self._activo = True


    @property 
    def activo(self):
        return self._activo
    
    @activo.setter
    def activo(self, valor):
        if not isinstance(valor, bool):
            raise ValueError("El estado del cliente debe ser booleano")
        self._activo = valor



