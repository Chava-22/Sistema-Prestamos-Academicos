from pydantic import ValidationError

from cliente import ClienteMayorista, ClienteMinorista
from usuario import Usuario
from equipo import Equipo
from prestamo import Prestamo
from catalogo import CatalogoProductos, mensaje_error_validacion
from gestor_solicitudes import GestorSolicitudes


def crear_usuarios():
    andres = Usuario(
        cedula="1001", nombre="Andrés", correo="andres@uees.edu.ec",
        carrera="Ingeniería", cliente=ClienteMayorista(),
    )
    maria = Usuario(
        cedula="1002", nombre="María", correo="maria@uees.edu.ec",
        carrera="Administración", cliente=ClienteMinorista(),
    )
    return andres, maria


def mostrar_usuario(usuario):
    print(f"Cédula: {usuario.get_cedula()}")
    print(f"Nombre: {usuario.get_nombre()}")
    print(f"Correo: {usuario.get_correo()}")
    print(f"Carrera: {usuario.get_carrera()}")
    print(f"Tipo de cliente: {type(usuario.get_cliente()).__name__}")


def mostrar_equipo(equipo):
    print(f"Código: {equipo.get_codigo()} | Nombre: {equipo.get_nombre()} | "
          f"Marca: {equipo.get_marca()} | Estado: {equipo.get_estado()}")


def demostrar_prestamos():
    print("Sistema de Préstamos Académicos\n")

    andres, maria = crear_usuarios()
    laptop = Equipo(codigo="EQ001", nombre="Laptop", marca="HP", estado="Disponible")
    proyector = Equipo(codigo="EQ002", nombre="Proyector", marca="Epson", estado="Disponible")

    prestamo_andres = Prestamo(andres, laptop, "21/08/2026", "Pendiente")
    prestamo_maria = Prestamo(maria, proyector, "21/08/2026", "Pendiente")

    print("Usuarios registrados")
    mostrar_usuario(andres)
    print()
    mostrar_usuario(maria)

    print("\nRealizando préstamos")
    prestamo_andres.realizar_prestamo()
    prestamo_maria.realizar_prestamo()

    print("\nDevolución de Andrés (3 días de atraso)")
    prestamo_andres.realizar_devolucion("25/08/2026", dias_atraso=3)

    print("\nDevolución de María (3 días de atraso)")
    prestamo_maria.realizar_devolucion("25/08/2026", dias_atraso=3)


def demostrar_catalogo():
    print("\n\nCatálogo de productos (Semana 5)\n")

    catalogo = CatalogoProductos()

    catalogo.agregar_producto(Equipo(codigo="EQ001", nombre="Laptop", marca="HP", estado="Disponible"))
    catalogo.agregar_producto(Equipo(codigo="EQ002", nombre="Proyector", marca="Epson", estado="Disponible"))
    catalogo.agregar_producto(Equipo(codigo="EQ003", nombre="Tablet", marca="Samsung", estado="Disponible"))

    print("Productos registrados:")
    for equipo in catalogo.listar_productos():
        mostrar_equipo(equipo)

    print("\nIntentando registrar un código duplicado (EQ001)")
    try:
        catalogo.agregar_producto(Equipo(codigo="EQ001", nombre="Laptop 2", marca="Dell", estado="Disponible"))
    except ValueError as error:
        print(f"Error controlado: {error}")

    print("\nBuscando el producto EQ002")
    encontrado = catalogo.buscar_producto("EQ002")
    mostrar_equipo(encontrado)

    print("\nActualizando el estado de EQ002 a 'Prestado'")
    catalogo.actualizar_producto("EQ002", estado="Prestado")
    mostrar_equipo(catalogo.buscar_producto("EQ002"))

    print("\nEliminando el producto EQ003")
    catalogo.eliminar_producto("EQ003")

    print("\nListado final del catálogo:")
    for equipo in catalogo.listar_productos():
        mostrar_equipo(equipo)

    print(f"\nTotal de productos en el catálogo: {catalogo.total_productos()}")


def demostrar_validaciones_pydantic():
    print("\n\nValidación automática con Pydantic\n")

    print("Intentando crear un equipo con código vacío:")
    try:
        Equipo(codigo="", nombre="Laptop", marca="HP", estado="Disponible")
    except ValidationError as error:
        print(f"Error controlado: {mensaje_error_validacion(error)}")

    print("\nIntentando crear un equipo con un estado inválido:")
    try:
        Equipo(codigo="EQ099", nombre="Router", marca="TP-Link", estado="Perdido")
    except ValidationError as error:
        print(f"Error controlado: {mensaje_error_validacion(error)}")

    print("\nIntentando crear un cliente mayorista con un porcentaje fuera de rango:")
    try:
        ClienteMayorista(porcentaje_descuento=150)
    except ValidationError as error:
        print(f"Error controlado: {mensaje_error_validacion(error)}")


def demostrar_cola_solicitudes():
    print("\n\nCola de solicitudes en espera (Semana 7)\n")

    gestor = GestorSolicitudes()

    gestor.solicitar_equipo("1001", "Andrés", "EQ001", "01/09/2026")
    gestor.solicitar_equipo("1002", "María", "EQ001", "01/09/2026")
    gestor.solicitar_equipo("1003", "Carlos", "EQ002", "02/09/2026")

    print(f"Solicitudes en espera: {gestor.total_solicitudes()}")

    print("\nPróxima solicitud a atender (sin quitarla de la fila):")
    siguiente = gestor.consultar_siguiente()
    print(f"  {siguiente.get_nombre_usuario()} pidió el equipo {siguiente.get_codigo_equipo()} "
          f"el {siguiente.get_fecha_solicitud()}")

    print("\nAtendiendo solicitudes en orden de llegada:")
    while gestor.hay_solicitudes_pendientes():
        atendida = gestor.atender_siguiente()
        print(f"  Atendida: {atendida.get_nombre_usuario()} - equipo {atendida.get_codigo_equipo()}")

    print("\nIntentando atender una solicitud cuando ya no hay ninguna:")
    try:
        gestor.atender_siguiente()
    except ValueError as error:
        print(f"Error controlado: {error}")


def main():
    demostrar_prestamos()
    demostrar_catalogo()
    demostrar_validaciones_pydantic()
    demostrar_cola_solicitudes()


if __name__ == "__main__":
    main()
