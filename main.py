class Persona:
    def __init__(self, cedula, nombre, correo):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__correo = correo

    def get_cedula(self):
        return self.__cedula

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_correo(self):
        return self.__correo

    def set_correo(self, correo):
        self.__correo = correo


class Usuario(Persona):
    def __init__(self, cedula, nombre, correo, carrera):
        super().__init__(cedula, nombre, correo)
        self.__carrera = carrera

    def get_carrera(self):
        return self.__carrera

    def set_carrera(self, carrera):
        self.__carrera = carrera


class Equipo:
    def __init__(self, codigo, nombre, marca, estado):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__marca = marca
        self.__estado = estado

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado


class Prestamo:
    def __init__(self, usuario, equipo, fecha, estado):
        self.__usuario = usuario
        self.__equipo = equipo
        self.__fecha = fecha
        self.__estado = estado
        self.__fecha_devolucion = "Sin devolución"

    def get_usuario(self):
        return self.__usuario

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_equipo(self):
        return self.__equipo

    def set_equipo(self, equipo):
        self.__equipo = equipo

    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def get_estado(self):
        return self.__estado

    def set_estado(self, estado):
        self.__estado = estado

    def get_fecha_devolucion(self):
        return self.__fecha_devolucion

    def set_fecha_devolucion(self, fecha_devolucion):
        self.__fecha_devolucion = fecha_devolucion

    def realizar_prestamo(self):
        if self.__equipo.get_estado() == "Disponible":
            self.__equipo.set_estado("Prestado")
            self.__estado = "Activo"
            print("Préstamo realizado correctamente")
        else:
            print("El equipo no está disponible")

    def realizar_devolucion(self, fecha_devolucion):
        if self.__equipo.get_estado() == "Prestado":
            self.__equipo.set_estado("Disponible")
            self.__estado = "Devuelto"
            self.__fecha_devolucion = fecha_devolucion
            print("Devolución realizada correctamente")
        else:
            print("El equipo ya está disponible")


usuario1 = Usuario(
    "1001",
    "Andrés",
    "andres@uees.edu.ec",
    "Ingeniería"
)

usuario2 = Usuario(
    "1002",
    "María",
    "maria@uees.edu.ec",
    "Administración"
)

equipo1 = Equipo(
    "EQ001",
    "Laptop",
    "HP",
    "Disponible"
)

equipo2 = Equipo(
    "EQ002",
    "Proyector",
    "Epson",
    "Disponible"
)

prestamo1 = Prestamo(
    usuario1,
    equipo1,
    "21/08/2026",
    "Pendiente"
)

prestamo2 = Prestamo(
    usuario2,
    equipo2,
    "21/08/2026",
    "Pendiente"
)


print("SISTEMA DE PRÉSTAMOS ACADÉMICOS")

print("\nUSUARIOS")

print("\nUsuario 1")
print("Cédula:", usuario1.get_cedula())
print("Nombre:", usuario1.get_nombre())
print("Correo:", usuario1.get_correo())
print("Carrera:", usuario1.get_carrera())

print("\nUsuario 2")
print("Cédula:", usuario2.get_cedula())
print("Nombre:", usuario2.get_nombre())
print("Correo:", usuario2.get_correo())
print("Carrera:", usuario2.get_carrera())


print("\nEQUIPOS")

print("\nEquipo 1")
print("Código:", equipo1.get_codigo())
print("Equipo:", equipo1.get_nombre())
print("Marca:", equipo1.get_marca())
print("Estado:", equipo1.get_estado())

print("\nEquipo 2")
print("Código:", equipo2.get_codigo())
print("Equipo:", equipo2.get_nombre())
print("Marca:", equipo2.get_marca())
print("Estado:", equipo2.get_estado())


print("\nPRÉSTAMOS")

print("\nPréstamo 1")
print("Usuario:", prestamo1.get_usuario().get_nombre())
print("Equipo:", prestamo1.get_equipo().get_nombre())
print("Fecha:", prestamo1.get_fecha())
print("Estado:", prestamo1.get_estado())

print("\nPréstamo 2")
print("Usuario:", prestamo2.get_usuario().get_nombre())
print("Equipo:", prestamo2.get_equipo().get_nombre())
print("Fecha:", prestamo2.get_fecha())
print("Estado:", prestamo2.get_estado())


print("\nREALIZANDO PRÉSTAMOS")

prestamo1.realizar_prestamo()
prestamo2.realizar_prestamo()


print("\nESTADO DE LOS EQUIPOS")

print("Laptop:", equipo1.get_estado())
print("Proyector:", equipo2.get_estado())


print("\nREALIZANDO DEVOLUCIÓN")

prestamo1.realizar_devolucion("21/08/2026")


print("\nESTADO FINAL")

print("Laptop:", equipo1.get_estado())
print("Estado del préstamo 1:", prestamo1.get_estado())
print("Fecha de devolución:", prestamo1.get_fecha_devolucion())

print("Proyector:", equipo2.get_estado())
print("Estado del préstamo 2:", prestamo2.get_estado())
print("Fecha de devolución:", prestamo2.get_fecha_devolucion())