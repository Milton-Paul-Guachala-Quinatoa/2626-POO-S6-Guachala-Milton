from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def mostrar_menu():
    """
    Muestra el menú principal del sistema.
    """

    print("\n========================================")
    print("      SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("========================================")
    print("1. Registrar platillo")
    print("2. Registrar bebida")
    print("3. Mostrar productos")
    print("4. Cambiar precio de un producto")
    print("5. Salir")
    print("========================================")


def registrar_platillo(restaurante):
    """
    Solicita los datos de un platillo y lo registra.
    """

    print("\n=== REGISTRAR PLATILLO ===")

    nombre = input("Nombre: ")
    tipo_platillo = input("Tipo de platillo: ")

    try:
        precio = float(input("Precio: "))
        calorias = int(input("Calorías: "))

        platillo = Platillo(
            nombre,
            precio,
            True,
            calorias,
            tipo_platillo
        )

        restaurante.registrar_producto(platillo)

    except ValueError:
        print("\nError: El precio y las calorías deben ser números.")


def registrar_bebida(restaurante):
    """
    Solicita los datos de una bebida y la registra.
    """

    print("\n=== REGISTRAR BEBIDA ===")

    nombre = input("Nombre: ")
    tipo_bebida = input("Tipo de bebida: ")

    try:
        precio = float(input("Precio: "))
        volumen_ml = int(input("Volumen en ml: "))

        bebida = Bebida(
            nombre,
            precio,
            True,
            volumen_ml,
            tipo_bebida
        )

        restaurante.registrar_producto(bebida)

    except ValueError:
        print("\nError: El precio y el volumen deben ser números.")


def cambiar_precio_producto(restaurante):
    """
    Permite modificar el precio de un producto registrado.
    """

    if not restaurante.productos:
        print("\nNo existen productos registrados.")
        return

    print("\n=== CAMBIAR PRECIO ===")

    for posicion, producto in enumerate(restaurante.productos):
        print(f"{posicion + 1}. {producto.nombre}")

    try:
        opcion = int(input("Seleccione un producto: "))
        nuevo_precio = float(input("Nuevo precio: "))

        producto_seleccionado = restaurante.productos[opcion - 1]
        producto_seleccionado.cambiar_precio(nuevo_precio)

    except ValueError:
        print("\nError: Debe ingresar valores numéricos.")

    except IndexError:
        print("\nError: Producto no encontrado.")


def main():
    """
    Punto de entrada del sistema.
    """

    restaurante = Restaurante()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            registrar_platillo(restaurante)

        elif opcion == "2":

            registrar_bebida(restaurante)

        elif opcion == "3":

            restaurante.mostrar_productos()

        elif opcion == "4":

            cambiar_precio_producto(restaurante)

        elif opcion == "5":

            print("\nGracias por utilizar nuestro sistema que tengas un excelente día.")
            break

        else:

            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()