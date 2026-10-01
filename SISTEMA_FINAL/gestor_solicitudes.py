from cola_solicitudes import ColaSolicitudes
from solicitud import SolicitudPrestamo


class GestorSolicitudes:
    """
    Administra la fila de espera de solicitudes de préstamo.

    Usa ColaSolicitudes (el tipo de dato abstracto lineal) para decidir el
    orden de atención, y delega el guardado y la carga de datos al
    Repository que reciba, sin encargarse él mismo de leer o escribir
    archivos.
    """

    def __init__(self, repositorio=None):
        self.__cola = ColaSolicitudes()
        self.__repositorio = repositorio

        if self.__repositorio:
            for solicitud in self.__repositorio.cargar_todas():
                self.__cola.encolar(solicitud)

    def __guardar_cambios(self):
        if self.__repositorio:
            self.__repositorio.guardar_todas(self.__cola.listar())

    def solicitar_equipo(self, cedula_usuario, nombre_usuario, codigo_equipo, fecha_solicitud):
        solicitud = SolicitudPrestamo(
            cedula_usuario=cedula_usuario,
            nombre_usuario=nombre_usuario,
            codigo_equipo=codigo_equipo,
            fecha_solicitud=fecha_solicitud,
        )
        self.__cola.encolar(solicitud)
        self.__guardar_cambios()
        return solicitud

    def atender_siguiente(self):
        if self.__cola.esta_vacia():
            raise ValueError("No hay solicitudes en espera por atender")
        solicitud = self.__cola.desencolar()
        self.__guardar_cambios()
        return solicitud

    def consultar_siguiente(self):
        if self.__cola.esta_vacia():
            return None
        return self.__cola.consultar_siguiente()

    def hay_solicitudes_pendientes(self):
        return not self.__cola.esta_vacia()

    def total_solicitudes(self):
        return self.__cola.cantidad()

    def listar_solicitudes(self):
        return self.__cola.listar()
