class Prestamo:
    """
    Relaciona un Usuario con un Equipo durante un periodo de tiempo.
    Al haber atraso en la devolución, la multa base se ajusta según
    el tipo real de Cliente del usuario (polimorfismo).
    """

    MULTA_POR_DIA = 5

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
        if self.__equipo.get_estado() != "Disponible":
            print("El equipo no está disponible")
            return

        self.__equipo.set_estado("Prestado")
        self.__estado = "Activo"
        print("Préstamo realizado correctamente")

    def realizar_devolucion(self, fecha_devolucion, dias_atraso=0):
        if self.__equipo.get_estado() != "Prestado":
            print("El equipo ya está disponible")
            return

        self.__equipo.set_estado("Disponible")
        self.__estado = "Devuelto"
        self.__fecha_devolucion = fecha_devolucion
        print("Devolución realizada correctamente")

        if dias_atraso > 0:
            self.__cobrar_multa(dias_atraso)

    def __cobrar_multa(self, dias_atraso):
        multa_base = dias_atraso * self.MULTA_POR_DIA
        cliente = self.__usuario.get_cliente()

        # Polimorfismo: no se pregunta si el cliente es mayorista o
        # minorista, simplemente se delega el cálculo a su propia clase.
        multa_final = cliente.calcularDescuento(multa_base)

        print(f"Días de atraso: {dias_atraso}")
        print(f"Multa base: ${multa_base}")
        print(f"Tipo de cliente: {type(cliente).__name__}")
        print(f"Multa final aplicada: ${multa_final:.2f}")
