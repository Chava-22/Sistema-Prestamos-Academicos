from pydantic import ValidationError


def mensaje_error_validacion(error: ValidationError) -> str:
    """Convierte el primer error de Pydantic en un mensaje simple y legible."""
    primero = error.errors()[0]
    campo = primero["loc"][0] if primero["loc"] else "dato"
    return f"{campo}: {primero['msg']}"


class CatalogoProductos:
    """
    Administra el catálogo de equipos (productos) disponibles para préstamo.

    Usa tres colecciones con un propósito distinto cada una:
    - list: mantiene el orden en que se registraron los productos, útil para listarlos.
    - dict: permite buscar un producto por su código en tiempo constante.
    - set: guarda los códigos ya registrados, para detectar duplicados antes de insertar.

    La lógica de negocio (duplicados, búsquedas, actualizaciones) vive aquí.
    Guardar y cargar los datos del disco es responsabilidad de un Repository
    externo (ver repositorio_productos.py), que este catálogo solo utiliza
    sin conocer sus detalles internos — así se separa el acceso a los datos
    de la lógica principal de la aplicación (patrón Repository).
    """

    def __init__(self, repositorio=None):
        self.__productos = []
        self.__productos_por_codigo = {}
        self.__codigos_registrados = set()
        self.__repositorio = repositorio

        if self.__repositorio:
            for equipo in self.__repositorio.cargar_todos():
                self.__registrar_en_memoria(equipo)

    def __registrar_en_memoria(self, equipo):
        codigo = equipo.get_codigo()
        if codigo in self.__codigos_registrados:
            return
        self.__productos.append(equipo)
        self.__productos_por_codigo[codigo] = equipo
        self.__codigos_registrados.add(codigo)

    def __guardar_cambios(self):
        if self.__repositorio:
            self.__repositorio.guardar_todos(self.__productos)

    def agregar_producto(self, equipo):
        codigo = equipo.get_codigo()
        if codigo in self.__codigos_registrados:
            raise ValueError(f"Ya existe un producto registrado con el código {codigo}")

        self.__registrar_en_memoria(equipo)
        self.__guardar_cambios()

    def buscar_producto(self, codigo):
        return self.__productos_por_codigo.get(codigo)

    def listar_productos(self):
        return list(self.__productos)

    def actualizar_producto(self, codigo, nombre=None, marca=None, estado=None):
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con el código {codigo}")

        try:
            if nombre:
                producto.set_nombre(nombre)
            if marca:
                producto.set_marca(marca)
            if estado:
                producto.set_estado(estado)
        except ValidationError as error:
            raise ValueError(mensaje_error_validacion(error)) from error

        self.__guardar_cambios()
        return producto

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con el código {codigo}")

        self.__productos.remove(producto)
        del self.__productos_por_codigo[codigo]
        self.__codigos_registrados.discard(codigo)
        self.__guardar_cambios()

        return producto

    def existe_codigo(self, codigo):
        return codigo in self.__codigos_registrados

    def total_productos(self):
        return len(self.__productos)
