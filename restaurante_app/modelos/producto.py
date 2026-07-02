class Producto:
    """
    Representa un producto general del restaurante.

    Esta clase actúa como clase padre para demostrar
    herencia y encapsulación.
    """

    def __init__(self, nombre, precio, disponible):
        """
        Inicializa un producto del restaurante.
        """

        self.nombre = nombre
        self.__precio = precio
        self.disponible = disponible

    def obtener_precio(self):
        """
        Devuelve el precio encapsulado del producto.
        """

        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        """
        Actualiza el precio si es mayor que cero.
        """

        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            print("\nPrecio actualizado correctamente.")
        else:
            print("\nError: El precio debe ser mayor que cero.")

    def mostrar_informacion(self):
        """
        Muestra la información general del producto.

        Este método será sobrescrito por las clases hijas.
        """

        estado = "Disponible" if self.disponible else "No disponible"

        print("\n=== PRODUCTO ===")
        print(f"Nombre        : {self.nombre}")
        print(f"Precio        : ${self.__precio:.2f}")
        print(f"Disponibilidad: {estado}")