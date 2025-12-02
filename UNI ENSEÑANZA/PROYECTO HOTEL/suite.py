from habitacion import Habitacion


class Suite(Habitacion):

    # Realizamos los principios de herencia con super
    # Colocamos los atributos de la clase padre + clase hija

    def __init__(self, numero, capacidad, precio_por_noche, disponible, jacuzzi):
        # Validaciones
        if not isinstance(jacuzzi, bool):
            raise ValueError(
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
