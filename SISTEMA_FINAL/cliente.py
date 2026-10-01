from abc import ABC, abstractmethod

from pydantic import BaseModel, ConfigDict, Field


class Cliente(BaseModel, ABC):
    model_config = ConfigDict(validate_assignment=True)

    @abstractmethod
    def calcularDescuento(self, monto: float) -> float:
        ...


class ClienteMayorista(Cliente):
    porcentaje_descuento: float = Field(default=20, ge=0, le=100)

    def get_porcentaje_descuento(self):
        return self.porcentaje_descuento

    def set_porcentaje_descuento(self, porcentaje_descuento):
        self.porcentaje_descuento = porcentaje_descuento

    def calcularDescuento(self, monto: float) -> float:
        descuento = monto * (self.porcentaje_descuento / 100)
        return monto - descuento


class ClienteMinorista(Cliente):
    porcentaje_descuento: float = Field(default=5, ge=0, le=100)

    def get_porcentaje_descuento(self):
        return self.porcentaje_descuento

    def set_porcentaje_descuento(self, porcentaje_descuento):
        self.porcentaje_descuento = porcentaje_descuento

    def calcularDescuento(self, monto: float) -> float:
        descuento = monto * (self.porcentaje_descuento / 100)
        return monto - descuento
