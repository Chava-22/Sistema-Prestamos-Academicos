import pytest

from cola_solicitudes import ColaSolicitudes


def test_cola_nueva_esta_vacia():
    cola = ColaSolicitudes()
    assert cola.esta_vacia() is True
    assert cola.cantidad() == 0


def test_encolar_agrega_elementos_en_orden():
    cola = ColaSolicitudes()
    cola.encolar("A")
    cola.encolar("B")
    cola.encolar("C")

    assert cola.cantidad() == 3
    assert cola.esta_vacia() is False
    assert cola.listar() == ["A", "B", "C"]


def test_desencolar_respeta_orden_fifo():
    cola = ColaSolicitudes()
    cola.encolar("primero")
    cola.encolar("segundo")

    assert cola.desencolar() == "primero"
    assert cola.desencolar() == "segundo"
    assert cola.esta_vacia() is True


def test_consultar_siguiente_no_elimina_el_elemento():
    cola = ColaSolicitudes()
    cola.encolar("único")

    assert cola.consultar_siguiente() == "único"
    assert cola.cantidad() == 1  # sigue estando en la cola


def test_desencolar_cola_vacia_lanza_error():
    cola = ColaSolicitudes()
    with pytest.raises(IndexError):
        cola.desencolar()


def test_consultar_siguiente_cola_vacia_lanza_error():
    cola = ColaSolicitudes()
    with pytest.raises(IndexError):
        cola.consultar_siguiente()


def test_cantidad_disminuye_al_desencolar():
    cola = ColaSolicitudes()
    cola.encolar(1)
    cola.encolar(2)
    cola.desencolar()

    assert cola.cantidad() == 1
