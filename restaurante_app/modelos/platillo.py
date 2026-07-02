from modelos.producto import Producto


class Platillo(Producto):
    """
    Representa un platillo del restaurante.

    Hereda los atributos y métodos de Producto e incorpora
    información propia de una comida.
    """

    def __init__(self, nombre, precio, disponible, calorias, tipo_platillo):
        """
        Inicializa un nuevo platillo.
        """

        super().__init__(nombre, precio, disponible)

        self.calorias = calorias
        self.tipo_platillo = tipo_platillo

    def mostrar_informacion(self):
        """
        Muestra la información del platillo.

        Sobrescribe el método de Producto para demostrar
        polimorfismo.
        """

        estado = "Disponible" if self.disponible else "No disponible"

        print("\n=== PLATILLO ===")
        print(f"Nombre        : {self.nombre}")
        print(f"Tipo          : {self.tipo_platillo}")
        print(f"Calorías      : {self.calorias}")
        print(f"Precio        : ${self.obtener_precio():.2f}")
        print(f"Disponibilidad: {estado}")