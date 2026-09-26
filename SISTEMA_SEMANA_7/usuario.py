from pydantic import ConfigDict, field_validator

from persona import Persona
from cliente import Cliente


class Usuario(Persona):
    model_config = ConfigDict(validate_assignment=True, arbitrary_types_allowed=True)

    carrera: str
    cliente: Cliente

    @field_validator("carrera")
    @classmethod
    def carrera_no_vacia(cls, valor):
        if not valor or not valor.strip():
            raise ValueError("La carrera no puede estar vacía")
        return valor

    def get_carrera(self):
        return self.carrera

    def set_carrera(self, carrera):
        self.carrera = carrera

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, cliente: Cliente):
        self.cliente = cliente
