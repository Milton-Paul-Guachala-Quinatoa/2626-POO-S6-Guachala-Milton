class Restaurante:
    """
    Gestiona los productos del restaurante.

    Esta clase pertenece a la capa de servicios y se encarga
    de administrar una lista de productos registrados.
    """

    def __init__(self):
        """
        Inicializa la lista de productos.
        """

        self.productos = []

    def registrar_producto(self, producto):
        """
        Registra un platillo o bebida en la lista.
        """

        self.productos.append(producto)
        print("\nProducto registrado correctamente.")

    def mostrar_productos(self):
        """
        Muestra todos los productos registrados.

        Aquí se demuestra polimorfismo, porque cada objeto
        ejecuta su propio método mostrar_informacion().
        """

        print("\n======= PRODUCTOS DEL RESTAURANTE =======")

        if not self.productos:
            print("No existen productos registrados.")
            return

        print("\nDemostración del polimorfismo:")

        for producto in self.productos:
            producto.mostrar_informacion()