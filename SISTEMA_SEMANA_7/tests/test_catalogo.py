import pytest

from catalogo import CatalogoProductos
from equipo import Equipo


def test_agregar_y_buscar_producto():
    catalogo = CatalogoProductos()
    catalogo.agregar_producto(Equipo(codigo="EQ001", nombre="Laptop", marca="HP", estado="Disponible"))

    encontrado = catalogo.buscar_producto("EQ001")

    assert encontrado is not None
    assert encontrado.get_nombre() == "Laptop"


def test_no_permite_codigos_duplicados():
    catalogo = CatalogoProductos()
    catalogo.agregar_producto(Equipo(codigo="EQ001", nombre="Laptop", marca="HP", estado="Disponible"))

    with pytest.raises(ValueError):
        catalogo.agregar_producto(Equipo(codigo="EQ001", nombre="Otra", marca="Dell", estado="Disponible"))


def test_actualizar_y_eliminar_producto():
    catalogo = CatalogoProductos()
    catalogo.agregar_producto(Equipo(codigo="EQ001", nombre="Laptop", marca="HP", estado="Disponible"))

    catalogo.actualizar_producto("EQ001", estado="Prestado")
    assert catalogo.buscar_producto("EQ001").get_estado() == "Prestado"

    catalogo.eliminar_producto("EQ001")
    assert catalogo.buscar_producto("EQ001") is None
    assert catalogo.total_productos() == 0
