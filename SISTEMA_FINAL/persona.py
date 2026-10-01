from pydantic import BaseModel, ConfigDict, field_validator


class Persona(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    cedula: str
    nombre: str
    correo: str

    @field_validator("cedula", "nombre")
    @classmethod
    def campo_no_vacio(cls, valor, info):
        if not valor or not valor.strip():
            raise ValueError(f"El campo '{info.field_name}' no puede estar vacío")
        return valor

    @field_validator("correo")
    @classmethod
    def correo_valido(cls, valor):
        if "@" not in valor:
            raise ValueError("El correo no tiene un formato válido")
        return valor

    def get_cedula(self):
        return self.cedula

    def set_cedula(self, cedula):
        self.cedula = cedula

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_correo(self):
        return self.correo

    def set_correo(self, correo):
        self.correo = correo
