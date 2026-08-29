from cliente import ClienteMayorista, ClienteMinorista
from usuario import Usuario
from equipo import Equipo
from prestamo import Prestamo


def crear_usuarios():
    andres = Usuario("1001", "Andrés", "andres@uees.edu.ec", "Ingeniería", ClienteMayorista())
    maria = Usuario("1002", "María", "maria@uees.edu.ec", "Administración", ClienteMinorista())
    return andres, maria


def crear_equipos():
    laptop = Equipo("EQ001", "Laptop", "HP", "Disponible")
    proyector = Equipo("EQ002", "Proyector", "Epson", "Disponible")
    return laptop, proyector


def mostrar_usuario(usuario):
    print(f"Cédula: {usuario.get_cedula()}")
    print(f"Nombre: {usuario.get_nombre()}")
    print(f"Correo: {usuario.get_correo()}")
    print(f"Carrera: {usuario.get_carrera()}")
    print(f"Tipo de cliente: {type(usuario.get_cliente()).__name__}")


def mostrar_equipo(equipo):
    print(f"Código: {equipo.get_codigo()}")
    print(f"Equipo: {equipo.get_nombre()}")
    print(f"Marca: {equipo.get_marca()}")
    print(f"Estado: {equipo.get_estado()}")


def demostrar_polimorfismo():
    print("\nMismo método, mismo monto, distinto resultado según el tipo real de cliente:")
    monto_prueba = 100
    for cliente in (ClienteMayorista(), ClienteMinorista()):
        resultado = cliente.calcularDescuento(monto_prueba)
        print(f"{type(cliente).__name__}: descuento sobre ${monto_prueba} -> ${resultado:.2f}")


def main():
    print("Sistema de Préstamos Académicos\n")

    andres, maria = crear_usuarios()
    laptop, proyector = crear_equipos()

    prestamo_andres = Prestamo(andres, laptop, "21/08/2026", "Pendiente")
    prestamo_maria = Prestamo(maria, proyector, "21/08/2026", "Pendiente")

    print("Usuarios registrados")
    mostrar_usuario(andres)
    print()
    mostrar_usuario(maria)

    print("\nEquipos disponibles")
    mostrar_equipo(laptop)
    print()
    mostrar_equipo(proyector)

    print("\nRealizando préstamos")
    prestamo_andres.realizar_prestamo()
    prestamo_maria.realizar_prestamo()

    print("\nDevolución de Andrés (3 días de atraso)")
    prestamo_andres.realizar_devolucion("25/08/2026", dias_atraso=3)

    print("\nDevolución de María (3 días de atraso)")
    prestamo_maria.realizar_devolucion("25/08/2026", dias_atraso=3)

    demostrar_polimorfismo()


if __name__ == "__main__":
    main()
