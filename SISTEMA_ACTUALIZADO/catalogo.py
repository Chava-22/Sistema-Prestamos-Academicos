from pydantic import ValidationError


def mensaje_error_validacion(error: ValidationError) -> str:
    primero = error.errors()[0]
    campo = primero["loc"][0] if primero["loc"] else "dato"
    return f"{campo}: {primero['msg']}"


class CatalogoProductos:
    def __init__(self):
        self.__productos = []
        self.__productos_por_codigo = {}
        self.__codigos_registrados = set()

    def agregar_producto(self, equipo):
        codigo = equipo.get_codigo()
        if codigo in self.__codigos_registrados:
            raise ValueError(f"Ya existe un producto registrado con el código {codigo}")

        self.__productos.append(equipo)
        self.__productos_por_codigo[codigo] = equipo
        self.__codigos_registrados.add(codigo)

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

        return producto

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con el código {codigo}")

        self.__productos.remove(producto)
        del self.__productos_por_codigo[codigo]
        self.__codigos_registrados.discard(codigo)

        return producto

    def existe_codigo(self, codigo):
        return codigo in self.__codigos_registrados

    def total_productos(self):
        return len(self.__productos)
