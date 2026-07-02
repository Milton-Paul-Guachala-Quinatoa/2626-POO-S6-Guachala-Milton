from modelos.producto import Producto


class Bebida(Producto):
    """
    Representa una bebida del restaurante.

    Hereda los atributos y métodos de Producto e incorpora
    información propia de una bebida.
    """

    def __init__(self, nombre, precio, disponible, volumen_ml, tipo_bebida):
        """
        Inicializa una nueva bebida.
        """

        super().__init__(nombre, precio, disponible)

        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida

    def mostrar_informacion(self):
        """
        Muestra la información de la bebida.

        Sobrescribe el método de Producto para demostrar
        polimorfismo.
        """

        estado = "Disponible" if self.disponible else "No disponible"

        print("\n=== BEBIDA ===")
        print(f"Nombre        : {self.nombre}")
        print(f"Tipo          : {self.tipo_bebida}")
        print(f"Volumen       : {self.volumen_ml} ml")
        print(f"Precio        : ${self.obtener_precio():.2f}")
        print(f"Disponibilidad: {estado}")