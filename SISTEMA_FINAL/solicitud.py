from pydantic import BaseModel, ConfigDict, Field


class SolicitudPrestamo(BaseModel):
    """Solicitud de un usuario para pedir un equipo que en ese momento no está disponible."""

    model_config = ConfigDict(validate_assignment=True)

    cedula_usuario: str = Field(min_length=1)
    nombre_usuario: str = Field(min_length=1)
    codigo_equipo: str = Field(min_length=1)
    fecha_solicitud: str = Field(min_length=1)

    def get_cedula_usuario(self):
        return self.cedula_usuario

    def get_nombre_usuario(self):
        return self.nombre_usuario

    def get_codigo_equipo(self):
        return self.codigo_equipo

    def get_fecha_solicitud(self):
        return self.fecha_solicitud
