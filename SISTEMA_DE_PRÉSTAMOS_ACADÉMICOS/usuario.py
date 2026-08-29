from persona import Persona
from cliente import Cliente


class Usuario(Persona):
    """
    Estudiante o miembro de la universidad que puede solicitar equipos.
    Cada Usuario tiene asociado un Cliente (composición) que define
    cómo se le calculan los descuentos sobre las multas.
    """

    def __init__(self, cedula, nombre, correo, carrera, cliente: Cliente):
        super().__init__(cedula, nombre, correo)
        self.__carrera = carrera
        self.__cliente = cliente

    def get_carrera(self):
        return self.__carrera

    def set_carrera(self, carrera):
        self.__carrera = carrera

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, cliente: Cliente):
        self.__cliente = cliente
