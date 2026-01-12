from habitacion import Habitacion

from excepciones import DatosInvalidosError, TipoDatoError

class Suite(Habitacion):

    # Realizamos los principios de herencia con super
    # Colocamos los atributos de la clase padre + clase hija

    def __init__(self, numero:str, capacidad:int, precio_por_noche:float, jacuzzi:bool, disponible:bool = True):
        # Validaciones
        if not isinstance(jacuzzi, bool):
            raise TipoDatoError(
                "El valor de Jacuzzi debe ser un dato booleano (True o false)"
            )

        # Le pasamos a la clase padre lo que es suyo
        super().__init__(numero, capacidad, precio_por_noche, disponible)

        # Aqui solo llamamos el de la clase hija (suite)
        self.jacuzzi = jacuzzi

    # Método de suite
    def describir(self):
        super().describir()
        print(f"- Jacuzzi: {self.jacuzzi} ")

    def pago_extra(self):
        return super().pago_extra() + 50
    
    def to_dict(self):
        # 1. Obtenemos el diccionario base de la clase padre
        datos = super().to_dict()
        
        # 2. Le agregamos lo exclusivo de la Suite
        datos["jacuzzi"] = self.jacuzzi
        
        # 3. Lo devolvemos completo
        return datos