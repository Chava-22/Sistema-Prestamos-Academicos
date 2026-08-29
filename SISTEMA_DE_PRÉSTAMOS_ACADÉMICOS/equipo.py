class Equipo:
    """Recurso físico que la universidad presta a los usuarios."""

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
