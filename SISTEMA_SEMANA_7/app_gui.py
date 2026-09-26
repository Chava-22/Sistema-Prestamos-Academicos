from datetime import date
from pathlib import Path

import flet as ft
from pydantic import ValidationError

from catalogo import CatalogoProductos, mensaje_error_validacion
from equipo import Equipo
from repositorio_productos import RepositorioProductosJSON
from repositorio_solicitudes import RepositorioSolicitudesJSON
from gestor_solicitudes import GestorSolicitudes

CARPETA_PROYECTO = Path(__file__).resolve().parent
ARCHIVO_DATOS_PRODUCTOS = CARPETA_PROYECTO / "datos_catalogo.json"
ARCHIVO_DATOS_SOLICITUDES = CARPETA_PROYECTO / "datos_solicitudes.json"

# El catálogo y las solicitudes se guardan automáticamente a través de su
# Repository correspondiente, y se recargan solos cada vez que se abre la
# app: la información no se pierde al cerrar la ventana.
repositorio_productos = RepositorioProductosJSON(ARCHIVO_DATOS_PRODUCTOS)
catalogo = CatalogoProductos(repositorio=repositorio_productos)

repositorio_solicitudes = RepositorioSolicitudesJSON(ARCHIVO_DATOS_SOLICITUDES)
gestor_solicitudes = GestorSolicitudes(repositorio=repositorio_solicitudes)

COLOR_PRIMARIO = "#0F4C81"
COLOR_PRIMARIO_OSCURO = "#0B3A63"
COLOR_ACENTO = "#5FA8D3"
COLOR_FONDO = "#EEF2F6"
COLOR_TARJETA = "#FFFFFF"
COLOR_TEXTO = "#1B2430"
COLOR_TEXTO_SECUNDARIO = "#5C6672"
COLOR_TEXTO_SOBRE_PRIMARIO = "#FFFFFF"
COLOR_EXITO = "#1E7A4C"
COLOR_EXITO_FONDO = "#E4F5EC"
COLOR_ERROR = "#B3261E"
COLOR_ERROR_FONDO = "#FBEAEA"
COLOR_BORDE = "#DCE1E8"


def main(page: ft.Page):
    page.title = "Sistema de Préstamos Académicos"
    page.window_width = 980
    page.window_height = 820
    page.window_min_width = 820
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = COLOR_FONDO
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0
    page.theme = ft.Theme(color_scheme_seed=COLOR_PRIMARIO)
    page.assets_dir = "assets"

    encabezado = ft.Container(
        content=ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Image(src="logo.png", width=48, fit=ft.ImageFit.CONTAIN),
                            padding=ft.padding.only(right=4),
                        ),
                        ft.Column(
                            spacing=0,
                            controls=[
                                ft.Text(
                                    "Sistema de Préstamos Académicos",
                                    size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color=COLOR_TEXTO_SOBRE_PRIMARIO,
                                ),
                                ft.Text(
                                    "Catálogo de Productos",
                                    size=14,
                                    color="#CFE3F2",
                                ),
                            ],
                        ),
                    ],
                    spacing=16,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        bgcolor=COLOR_PRIMARIO,
        padding=ft.padding.symmetric(horizontal=32, vertical=26),
    )

    campo_codigo = ft.TextField(
        label="Código", width=170, border_radius=8, filled=True,
        color=COLOR_TEXTO, label_style=ft.TextStyle(color=COLOR_TEXTO_SECUNDARIO),
    )
    campo_nombre = ft.TextField(
        label="Nombre", width=210, border_radius=8, filled=True,
        color=COLOR_TEXTO, label_style=ft.TextStyle(color=COLOR_TEXTO_SECUNDARIO),
    )
    campo_marca = ft.TextField(
        label="Marca", width=170, border_radius=8, filled=True,
        color=COLOR_TEXTO, label_style=ft.TextStyle(color=COLOR_TEXTO_SECUNDARIO),
    )
    campo_estado = ft.Dropdown(
        label="Estado", width=170, border_radius=8, filled=True,
        color=COLOR_TEXTO, label_style=ft.TextStyle(color=COLOR_TEXTO_SECUNDARIO),
        options=[
            ft.dropdown.Option("Disponible"),
            ft.dropdown.Option("Prestado"),
        ],
    )

    campo_busqueda = ft.TextField(
        label="Buscar por código, nombre o marca",
        width=340, border_radius=8, filled=True, dense=True,
        prefix_icon=ft.Icons.SEARCH_ROUNDED,
        color=COLOR_TEXTO, label_style=ft.TextStyle(color=COLOR_TEXTO_SECUNDARIO),
    )

    icono_estado = ft.Icon(ft.Icons.INFO_OUTLINE, color=COLOR_TEXTO_SECUNDARIO, size=18)
    texto_estado = ft.Text(
        "Completa los campos y elige una acción.", size=13, color=COLOR_TEXTO_SECUNDARIO
    )
    banner_estado = ft.Container(
        content=ft.Row(controls=[icono_estado, texto_estado], spacing=8),
        bgcolor="#E4E9F0",
        border_radius=8,
        padding=ft.padding.symmetric(horizontal=14, vertical=10),
    )

    texto_total = ft.Text("0 producto(s)", size=13, weight=ft.FontWeight.W_600, color=COLOR_PRIMARIO_OSCURO)
    chip_total = ft.Container(
        content=texto_total,
        bgcolor="#DCE7F2",
        border_radius=20,
        padding=ft.padding.symmetric(horizontal=14, vertical=6),
    )

    def crear_tarjeta_stat(icono, color_icono, etiqueta):
        valor = ft.Text("0", size=24, weight=ft.FontWeight.BOLD, color=COLOR_TEXTO)
        tarjeta = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Icon(icono, color=color_icono, size=22),
                        bgcolor=COLOR_FONDO,
                        border_radius=10,
                        padding=10,
                    ),
                    ft.Column(
                        spacing=0,
                        controls=[
                            valor,
                            ft.Text(etiqueta, size=12, color=COLOR_TEXTO_SECUNDARIO),
                        ],
                    ),
                ],
                spacing=12,
            ),
            bgcolor=COLOR_TARJETA,
            border_radius=14,
            padding=18,
            expand=True,
            shadow=ft.BoxShadow(blur_radius=14, color="#00000014", offset=ft.Offset(0, 4)),
        )
        return tarjeta, valor

    tarjeta_stat_total, valor_stat_total = crear_tarjeta_stat(ft.Icons.INVENTORY_2_ROUNDED, COLOR_PRIMARIO, "Total de productos")
    tarjeta_stat_disponibles, valor_stat_disponibles = crear_tarjeta_stat(ft.Icons.CHECK_CIRCLE_ROUNDED, COLOR_EXITO, "Disponibles")
    tarjeta_stat_prestados, valor_stat_prestados = crear_tarjeta_stat(ft.Icons.SCHEDULE_ROUNDED, COLOR_ERROR, "Prestados")

    fila_stats = ft.Row(
        controls=[tarjeta_stat_total, tarjeta_stat_disponibles, tarjeta_stat_prestados],
        spacing=18,
    )

    tabla = ft.DataTable(
        heading_row_color="#E4E9F0",
        heading_text_style=ft.TextStyle(color=COLOR_TEXTO, weight=ft.FontWeight.BOLD),
        data_text_style=ft.TextStyle(color=COLOR_TEXTO),
        border=ft.border.all(1, COLOR_BORDE),
        border_radius=10,
        column_spacing=40,
        columns=[
            ft.DataColumn(ft.Text("Código")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Marca")),
            ft.DataColumn(ft.Text("Estado")),
        ],
        rows=[],
    )

    def mostrar_estado(texto, es_error):
        texto_estado.value = texto
        texto_estado.color = COLOR_ERROR if es_error else COLOR_EXITO
        icono_estado.name = ft.Icons.ERROR_OUTLINE if es_error else ft.Icons.CHECK_CIRCLE_OUTLINE
        icono_estado.color = COLOR_ERROR if es_error else COLOR_EXITO
        banner_estado.bgcolor = COLOR_ERROR_FONDO if es_error else COLOR_EXITO_FONDO
        page.update()

    def limpiar_campos():
        campo_codigo.value = ""
        campo_nombre.value = ""
        campo_marca.value = ""
        campo_estado.value = None

    def fila_estado(estado):
        color = COLOR_EXITO if estado == "Disponible" else COLOR_ERROR
        fondo = COLOR_EXITO_FONDO if estado == "Disponible" else COLOR_ERROR_FONDO
        return ft.Container(
            content=ft.Text(estado, size=12, color=color, weight=ft.FontWeight.W_600),
            bgcolor=fondo,
            border_radius=12,
            padding=ft.padding.symmetric(horizontal=10, vertical=4),
        )

    def actualizar_tabla():
        productos = catalogo.listar_productos()
        filtro = (campo_busqueda.value or "").strip().lower()
        if filtro:
            productos = [
                producto for producto in productos
                if filtro in producto.get_codigo().lower()
                or filtro in producto.get_nombre().lower()
                or filtro in producto.get_marca().lower()
            ]

        tabla.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(producto.get_codigo(), color=COLOR_TEXTO)),
                    ft.DataCell(ft.Text(producto.get_nombre(), color=COLOR_TEXTO)),
                    ft.DataCell(ft.Text(producto.get_marca(), color=COLOR_TEXTO)),
                    ft.DataCell(fila_estado(producto.get_estado())),
                ]
            )
            for producto in productos
        ]

        total = catalogo.total_productos()
        disponibles = sum(1 for producto in catalogo.listar_productos() if producto.get_estado() == "Disponible")
        prestados = total - disponibles

        texto_total.value = f"{total} producto(s)"
        valor_stat_total.value = str(total)
        valor_stat_disponibles.value = str(disponibles)
        valor_stat_prestados.value = str(prestados)

        page.update()

    def campos_validos():
        if not campo_codigo.value or not campo_nombre.value or not campo_marca.value:
            mostrar_estado("Código, nombre y marca son obligatorios.", es_error=True)
            return False
        return True

    def registrar_click(e):
        if not campos_validos():
            return
        try:
            nuevo_equipo = Equipo(
                codigo=campo_codigo.value,
                nombre=campo_nombre.value,
                marca=campo_marca.value,
                estado=campo_estado.value or "Disponible",
            )
            catalogo.agregar_producto(nuevo_equipo)
            mostrar_estado(f"Producto {nuevo_equipo.get_codigo()} agregado correctamente.", es_error=False)
            limpiar_campos()
            actualizar_tabla()
        except ValidationError as error:
            mostrar_estado(mensaje_error_validacion(error), es_error=True)
        except ValueError as error:
            mostrar_estado(str(error), es_error=True)

    def buscar_click(e):
        if not campo_codigo.value:
            mostrar_estado("Ingresa un código para buscar.", es_error=True)
            return
        producto = catalogo.buscar_producto(campo_codigo.value)
        if producto is None:
            mostrar_estado(f"No existe un producto con el código {campo_codigo.value}.", es_error=True)
            return
        campo_nombre.value = producto.get_nombre()
        campo_marca.value = producto.get_marca()
        campo_estado.value = producto.get_estado()
        mostrar_estado(f"Producto {producto.get_codigo()} encontrado.", es_error=False)
        page.update()

    def actualizar_click(e):
        if not campo_codigo.value:
            mostrar_estado("Ingresa el código del producto a actualizar.", es_error=True)
            return
        try:
            catalogo.actualizar_producto(
                campo_codigo.value,
                nombre=campo_nombre.value,
                marca=campo_marca.value,
                estado=campo_estado.value,
            )
            mostrar_estado(f"Producto {campo_codigo.value} actualizado correctamente.", es_error=False)
            actualizar_tabla()
        except ValueError as error:
            mostrar_estado(str(error), es_error=True)

    def eliminar_click(e):
        if not campo_codigo.value:
            mostrar_estado("Ingresa el código del producto a eliminar.", es_error=True)
            return
        try:
            catalogo.eliminar_producto(campo_codigo.value)
            mostrar_estado(f"Producto {campo_codigo.value} eliminado correctamente.", es_error=False)
            limpiar_campos()
            actualizar_tabla()
        except ValueError as error:
            mostrar_estado(str(error), es_error=True)

    def limpiar_click(e):
        limpiar_campos()
        mostrar_estado("Completa los campos y elige una acción.", es_error=False)
        texto_estado.color = COLOR_TEXTO_SECUNDARIO
        icono_estado.color = COLOR_TEXTO_SECUNDARIO
        icono_estado.name = ft.Icons.INFO_OUTLINE
        banner_estado.bgcolor = "#E4E9F0"
        page.update()

    def busqueda_cambiada(e):
        actualizar_tabla()

    campo_busqueda.on_change = busqueda_cambiada

    # ---------- Solicitudes en espera (Semana 7: cola FIFO + Repository) ----------
    campo_cedula_solicitud = ft.TextField(
        label="Cédula del solicitante", width=190, border_radius=8, filled=True,
        color=COLOR_TEXTO, label_style=ft.TextStyle(color=COLOR_TEXTO_SECUNDARIO),
    )
    campo_nombre_solicitud = ft.TextField(
        label="Nombre del solicitante", width=190, border_radius=8, filled=True,
        color=COLOR_TEXTO, label_style=ft.TextStyle(color=COLOR_TEXTO_SECUNDARIO),
    )
    campo_codigo_solicitud = ft.TextField(
        label="Código del equipo deseado", width=200, border_radius=8, filled=True,
        color=COLOR_TEXTO, label_style=ft.TextStyle(color=COLOR_TEXTO_SECUNDARIO),
    )

    texto_total_solicitudes = ft.Text("0 en espera", size=13, weight=ft.FontWeight.W_600, color=COLOR_PRIMARIO_OSCURO)
    chip_total_solicitudes = ft.Container(
        content=texto_total_solicitudes,
        bgcolor="#DCE7F2",
        border_radius=20,
        padding=ft.padding.symmetric(horizontal=14, vertical=6),
    )

    tabla_solicitudes = ft.DataTable(
        heading_row_color="#E4E9F0",
        heading_text_style=ft.TextStyle(color=COLOR_TEXTO, weight=ft.FontWeight.BOLD),
        data_text_style=ft.TextStyle(color=COLOR_TEXTO),
        border=ft.border.all(1, COLOR_BORDE),
        border_radius=10,
        column_spacing=40,
        columns=[
            ft.DataColumn(ft.Text("Turno")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Cédula")),
            ft.DataColumn(ft.Text("Equipo pedido")),
            ft.DataColumn(ft.Text("Fecha")),
        ],
        rows=[],
    )

    def actualizar_tabla_solicitudes():
        solicitudes = gestor_solicitudes.listar_solicitudes()
        tabla_solicitudes.rows = [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(indice + 1), color=COLOR_TEXTO)),
                    ft.DataCell(ft.Text(solicitud.get_nombre_usuario(), color=COLOR_TEXTO)),
                    ft.DataCell(ft.Text(solicitud.get_cedula_usuario(), color=COLOR_TEXTO)),
                    ft.DataCell(ft.Text(solicitud.get_codigo_equipo(), color=COLOR_TEXTO)),
                    ft.DataCell(ft.Text(solicitud.get_fecha_solicitud(), color=COLOR_TEXTO)),
                ]
            )
            for indice, solicitud in enumerate(solicitudes)
        ]
        texto_total_solicitudes.value = f"{gestor_solicitudes.total_solicitudes()} en espera"
        page.update()

    def agregar_solicitud_click(e):
        if not campo_cedula_solicitud.value or not campo_nombre_solicitud.value or not campo_codigo_solicitud.value:
            mostrar_estado("Completa cédula, nombre y código de equipo para la solicitud.", es_error=True)
            return
        try:
            fecha_hoy = date.today().strftime("%d/%m/%Y")
            gestor_solicitudes.solicitar_equipo(
                campo_cedula_solicitud.value,
                campo_nombre_solicitud.value,
                campo_codigo_solicitud.value,
                fecha_hoy,
            )
            mostrar_estado("Solicitud agregada al final de la fila de espera.", es_error=False)
            campo_cedula_solicitud.value = ""
            campo_nombre_solicitud.value = ""
            campo_codigo_solicitud.value = ""
            actualizar_tabla_solicitudes()
        except ValidationError as error:
            mostrar_estado(mensaje_error_validacion(error), es_error=True)

    def atender_siguiente_click(e):
        try:
            atendida = gestor_solicitudes.atender_siguiente()
            mostrar_estado(
                f"Se atendió a {atendida.get_nombre_usuario()} (equipo {atendida.get_codigo_equipo()}).",
                es_error=False,
            )
            actualizar_tabla_solicitudes()
        except ValueError as error:
            mostrar_estado(str(error), es_error=True)

    boton_agregar_solicitud = ft.ElevatedButton(
        "Agregar a la fila", icon=ft.Icons.PERSON_ADD_ALT_1_ROUNDED, on_click=agregar_solicitud_click,
        style=ft.ButtonStyle(
            bgcolor=COLOR_PRIMARIO,
            color=COLOR_TEXTO_SOBRE_PRIMARIO,
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
    )
    boton_atender_siguiente = ft.OutlinedButton(
        "Atender siguiente", icon=ft.Icons.SKIP_NEXT_ROUNDED, on_click=atender_siguiente_click,
        style=ft.ButtonStyle(color=COLOR_PRIMARIO_OSCURO),
    )

    boton_registrar = ft.ElevatedButton(
        "Registrar", icon=ft.Icons.ADD_ROUNDED, on_click=registrar_click,
        style=ft.ButtonStyle(
            bgcolor=COLOR_PRIMARIO,
            color=COLOR_TEXTO_SOBRE_PRIMARIO,
            shape=ft.RoundedRectangleBorder(radius=8),
        ),
    )
    boton_buscar = ft.OutlinedButton(
        "Buscar", icon=ft.Icons.SEARCH_ROUNDED, on_click=buscar_click,
        style=ft.ButtonStyle(color=COLOR_PRIMARIO_OSCURO),
    )
    boton_actualizar = ft.OutlinedButton(
        "Actualizar", icon=ft.Icons.EDIT_ROUNDED, on_click=actualizar_click,
        style=ft.ButtonStyle(color=COLOR_PRIMARIO_OSCURO),
    )
    boton_eliminar = ft.OutlinedButton(
        "Eliminar", icon=ft.Icons.DELETE_OUTLINE_ROUNDED, on_click=eliminar_click,
        style=ft.ButtonStyle(color=COLOR_ERROR),
    )
    boton_limpiar = ft.TextButton(
        "Limpiar campos", icon=ft.Icons.REFRESH_ROUNDED, on_click=limpiar_click,
        style=ft.ButtonStyle(color=COLOR_TEXTO_SECUNDARIO),
    )

    tarjeta_formulario = ft.Container(
        content=ft.Column(
            spacing=16,
            controls=[
                ft.Text("Registrar", size=15, weight=ft.FontWeight.BOLD, color=COLOR_TEXTO),
                ft.Row(controls=[campo_codigo, campo_nombre, campo_marca, campo_estado], wrap=True, spacing=14),
                ft.Row(
                    controls=[boton_registrar, boton_buscar, boton_actualizar, boton_eliminar, boton_limpiar],
                    spacing=10, wrap=True,
                ),
                banner_estado,
            ],
        ),
        bgcolor=COLOR_TARJETA,
        border_radius=14,
        padding=22,
        shadow=ft.BoxShadow(blur_radius=14, color="#00000014", offset=ft.Offset(0, 4)),
    )

    tarjeta_tabla = ft.Container(
        content=ft.Column(
            spacing=14,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Productos registrados", size=15, weight=ft.FontWeight.BOLD, color=COLOR_TEXTO),
                        chip_total,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                campo_busqueda,
                ft.Row(controls=[tabla], scroll=ft.ScrollMode.AUTO),
            ],
        ),
        bgcolor=COLOR_TARJETA,
        border_radius=14,
        padding=22,
        shadow=ft.BoxShadow(blur_radius=14, color="#00000014", offset=ft.Offset(0, 4)),
    )

    tarjeta_solicitudes = ft.Container(
        content=ft.Column(
            spacing=14,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Solicitudes en espera (fila FIFO)", size=15, weight=ft.FontWeight.BOLD, color=COLOR_TEXTO),
                        chip_total_solicitudes,
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Text(
                    "Cuando un equipo no está disponible, aquí se anota quién lo pidió. "
                    "Al presionar 'Atender siguiente' se atiende siempre a quien lleva más tiempo esperando.",
                    size=12, color=COLOR_TEXTO_SECUNDARIO,
                ),
                ft.Row(
                    controls=[campo_cedula_solicitud, campo_nombre_solicitud, campo_codigo_solicitud],
                    wrap=True, spacing=14,
                ),
                ft.Row(controls=[boton_agregar_solicitud, boton_atender_siguiente], spacing=10),
                ft.Row(controls=[tabla_solicitudes], scroll=ft.ScrollMode.AUTO),
            ],
        ),
        bgcolor=COLOR_TARJETA,
        border_radius=14,
        padding=22,
        shadow=ft.BoxShadow(blur_radius=14, color="#00000014", offset=ft.Offset(0, 4)),
    )

    page.add(
        encabezado,
        ft.Container(
            content=ft.Column(
                controls=[fila_stats, tarjeta_formulario, tarjeta_tabla, tarjeta_solicitudes],
                spacing=20,
            ),
            padding=ft.padding.symmetric(horizontal=32, vertical=26),
        ),
    )

    actualizar_tabla()
    actualizar_tabla_solicitudes()


if __name__ == "__main__":
    ft.app(target=main)
