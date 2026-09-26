import json
from pathlib import Path

from equipo import Equipo


class RepositorioProductosJSON:
    """
    Patrón Repository: guarda y recupera los productos (equipos) desde un
    archivo JSON. No sabe nada sobre duplicados, búsquedas ni ninguna otra
    regla de negocio; solo mueve datos entre los objetos Equipo y el
    archivo en disco. Esa separación es justamente el propósito del patrón
    Repository: la lógica principal (CatalogoProductos) no necesita saber
    cómo ni dónde se guardan los datos.
    """

    def __init__(self, ruta_archivo):
        self.__ruta_archivo = Path(ruta_archivo)

    def cargar_todos(self):
        if not self.__ruta_archivo.exists():
            return []

        try:
            contenido = self.__ruta_archivo.read_text(encoding="utf-8")
            datos = json.loads(contenido) if contenido.strip() else []
        except (json.JSONDecodeError, OSError):
            return []

        equipos = []
        for dato in datos:
            try:
                equipos.append(Equipo(**dato))
            except Exception:
                continue  # ignora registros corruptos o incompletos
        return equipos

    def guardar_todos(self, equipos):
        datos = [equipo.model_dump() for equipo in equipos]
        self.__ruta_archivo.write_text(
            json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8"
        )
