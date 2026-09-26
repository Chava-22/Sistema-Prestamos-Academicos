from repositorio_solicitudes import RepositorioSolicitudesJSON
from solicitud import SolicitudPrestamo


def test_cargar_todas_sin_archivo_devuelve_lista_vacia(tmp_path):
    repositorio = RepositorioSolicitudesJSON(tmp_path / "no_existe.json")
    assert repositorio.cargar_todas() == []


def test_guardar_y_cargar_mantiene_los_datos(tmp_path):
    archivo = tmp_path / "solicitudes.json"
    repositorio = RepositorioSolicitudesJSON(archivo)

    solicitud = SolicitudPrestamo(
        cedula_usuario="1001",
        nombre_usuario="Andrés",
        codigo_equipo="EQ001",
        fecha_solicitud="01/09/2026",
    )
    repositorio.guardar_todas([solicitud])

    solicitudes_cargadas = repositorio.cargar_todas()
    assert len(solicitudes_cargadas) == 1
    assert solicitudes_cargadas[0].get_codigo_equipo() == "EQ001"
    assert solicitudes_cargadas[0].get_nombre_usuario() == "Andrés"


def test_archivo_corrupto_devuelve_lista_vacia(tmp_path):
    archivo = tmp_path / "corrupto.json"
    archivo.write_text("esto no es json válido", encoding="utf-8")

    repositorio = RepositorioSolicitudesJSON(archivo)
    assert repositorio.cargar_todas() == []
