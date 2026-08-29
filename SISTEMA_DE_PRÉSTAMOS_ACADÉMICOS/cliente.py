from abc import ABC, abstractmethod


class Cliente(ABC):
    """
    Contrato que debe cumplir cualquier tipo de cliente del sistema.
    No se puede instanciar directamente: solo sirve como molde para
    ClienteMayorista y ClienteMinorista.
    """

    @abstractmethod
    def calcularDescuento(self, monto):
        """Devuelve el monto recibido ya con el descuento aplicado."""


class ClienteMayorista(Cliente):
    """Cliente que representa a una facultad o departamento (compra en volumen)."""

    def __init__(self, porcentaje_descuento=20):
        self.__porcentaje_descuento = porcentaje_descuento

    def get_porcentaje_descuento(self):
        return self.__porcentaje_descuento

    def set_porcentaje_descuento(self, porcentaje_descuento):
        self.__porcentaje_descuento = porcentaje_descuento

    def calcularDescuento(self, monto):
        descuento = monto * (self.__porcentaje_descuento / 100)
        return monto - descuento


class ClienteMinorista(Cliente):
    """Cliente que representa a un estudiante individual."""

    def __init__(self, porcentaje_descuento=5):
        self.__porcentaje_descuento = porcentaje_descuento

    def get_porcentaje_descuento(self):
        return self.__porcentaje_descuento

    def set_porcentaje_descuento(self, porcentaje_descuento):
        self.__porcentaje_descuento = porcentaje_descuento

    def calcularDescuento(self, monto):
        descuento = monto * (self.__porcentaje_descuento / 100)
        return monto - descuento
