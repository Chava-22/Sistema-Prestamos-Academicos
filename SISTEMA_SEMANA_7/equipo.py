from pydantic import BaseModel, ConfigDict, Field, field_validator

ESTADOS_VALIDOS = {"Disponible", "Prestado"}


class Equipo(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    codigo: str = Field(min_length=1)
    nombre: str = Field(min_length=1)
    marca: str = Field(min_length=1)
    estado: str = "Disponible"

    @field_validator("estado")
    @classmethod
    def estado_valido(cls, valor):
        if valor not in ESTADOS_VALIDOS:
            raise ValueError(f"Estado inválido: '{valor}'. Debe ser 'Disponible' o 'Prestado'")
        return valor

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado
