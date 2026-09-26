import json
from pathlib import Path

from solicitud import SolicitudPrestamo


class RepositorioSolicitudesJSON:
    """
    Patrón Repository: guarda y recupera solicitudes de préstamo desde un
    archivo JSON. No sabe nada sobre el orden de atención ni ninguna otra
    regla de negocio; solo mueve datos entre los objetos SolicitudPrestamo
    y el archivo en disco.
    """

    def __init__(self, ruta_archivo):
        self.__ruta_archivo = Path(ruta_archivo)

    def cargar_todas(self):
        if not self.__ruta_archivo.exists():
            return []

        try:
            contenido = self.__ruta_archivo.read_text(encoding="utf-8")
            datos = json.loads(contenido) if contenido.strip() else []
        except (json.JSONDecodeError, OSError):
            return []

        solicitudes = []
        for dato in datos:
            try:
                solicitudes.append(SolicitudPrestamo(**dato))
            except Exception:
                continue  # ignora registros corruptos o incompletos
        return solicitudes

    def guardar_todas(self, solicitudes):
        datos = [solicitud.model_dump() for solicitud in solicitudes]
        self.__ruta_archivo.write_text(
            json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8"
        )
