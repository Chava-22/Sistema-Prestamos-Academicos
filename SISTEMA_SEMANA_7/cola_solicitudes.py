class NodoCola:
    """Un eslabón de la cola: guarda un dato y una referencia al siguiente nodo."""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ColaSolicitudes:
    """
    Cola (FIFO) implementada a mano con una lista enlazada, sin usar
    collections.deque ni ninguna otra estructura de pila/cola de la
    biblioteca estándar de Python.

    Funciona bajo la regla "el primero en llegar es el primero en salir":
    quien se agrega primero, se atiende primero.
    """

    def __init__(self):
        self.__frente = None
        self.__final = None
        self.__cantidad = 0

    def encolar(self, dato):
        """Agrega un elemento al final de la cola."""
        nodo = NodoCola(dato)
        if self.esta_vacia():
            self.__frente = nodo
            self.__final = nodo
        else:
            self.__final.siguiente = nodo
            self.__final = nodo
        self.__cantidad += 1

    def desencolar(self):
        """Elimina y devuelve el elemento que lleva más tiempo esperando."""
        if self.esta_vacia():
            raise IndexError("No se puede desencolar: la cola está vacía")

        nodo = self.__frente
        self.__frente = nodo.siguiente
        if self.__frente is None:
            self.__final = None
        self.__cantidad -= 1
        return nodo.dato

    def consultar_siguiente(self):
        """Devuelve el próximo elemento a atender, sin eliminarlo de la cola."""
        if self.esta_vacia():
            raise IndexError("No se puede consultar: la cola está vacía")
        return self.__frente.dato

    def esta_vacia(self):
        return self.__cantidad == 0

    def cantidad(self):
        return self.__cantidad

    def listar(self):
        """Devuelve los elementos en orden, desde el próximo a atender hasta el último."""
        elementos = []
        actual = self.__frente
        while actual is not None:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos
