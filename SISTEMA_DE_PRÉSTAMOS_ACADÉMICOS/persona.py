class Persona:
    """Datos básicos comunes a cualquier persona registrada en el sistema."""

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
