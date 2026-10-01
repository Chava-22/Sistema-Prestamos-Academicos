import pytest

from gestor_solicitudes import GestorSolicitudes
from repositorio_solicitudes import RepositorioSolicitudesJSON


def test_solicitar_equipo_agrega_a_la_fila():
    gestor = GestorSolicitudes()
    gestor.solicitar_equipo("1001", "Andrés", "EQ001", "01/09/2026")

    assert gestor.total_solicitudes() == 1
    assert gestor.hay_solicitudes_pendientes() is True


def test_atender_siguiente_respeta_orden_de_llegada():
    gestor = GestorSolicitudes()
    gestor.solicitar_equipo("1001", "Andrés", "EQ001", "01/09/2026")
    gestor.solicitar_equipo("1002", "María", "EQ002", "02/09/2026")

    atendida = gestor.atender_siguiente()

    assert atendida.get_nombre_usuario() == "Andrés"
    assert gestor.total_solicitudes() == 1
    assert gestor.consultar_siguiente().get_nombre_usuario() == "María"


def test_atender_sin_solicitudes_lanza_error():
    gestor = GestorSolicitudes()
    with pytest.raises(ValueError):
        gestor.atender_siguiente()


def test_persistencia_con_repository(tmp_path):
    archivo = tmp_path / "solicitudes.json"
    repositorio = RepositorioSolicitudesJSON(archivo)

    gestor_1 = GestorSolicitudes(repositorio=repositorio)
    gestor_1.solicitar_equipo("1001", "Andrés", "EQ001", "01/09/2026")

    # Se crea un segundo gestor con el mismo repositorio, simulando que la
    # aplicación se cerró y se volvió a abrir: los datos deben seguir ahí.
    gestor_2 = GestorSolicitudes(repositorio=repositorio)

    assert gestor_2.total_solicitudes() == 1
    assert gestor_2.consultar_siguiente().get_codigo_equipo() == "EQ001"
