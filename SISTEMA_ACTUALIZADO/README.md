# Sistema de Préstamos Académicos

**Desarrollado por:** Andrés Calderón
**Universidad:** UEES
**Materia:** Programación Estructurada

---

## Descripción

**Sistema de Préstamos Académicos** es una aplicación de escritorio desarrollada para gestionar el catálogo de equipos tecnológicos de una institución educativa.

El sistema permite registrar, consultar, actualizar y eliminar equipos, además de controlar su disponibilidad y estado.

## Funcionalidades

* **Registrar equipos** con código, nombre, marca y estado.
* **Buscar equipos** mediante su código.
* **Actualizar información** de equipos registrados.
* **Eliminar equipos** del catálogo.
* **Consultar estadísticas** de equipos totales, disponibles y prestados.
* **Filtrar equipos** por código, nombre o marca.
* **Guardar automáticamente** la información para conservar los datos al cerrar y volver a abrir la aplicación.
* **Validar información** para evitar campos incompletos, códigos duplicados y estados no permitidos.

## Requisitos

* Python **3.9 o superior**.
* Dependencias del proyecto:

```bash
pip install pydantic flet
```

## Ejecución

Para iniciar la aplicación:

```bash
python app_gui.py
```

También puede ejecutarse la demostración por consola:

```bash
python main.py
```

## Estructura del proyecto

| Archivo               | Descripción                                  |
| --------------------- | -------------------------------------------- |
| `app_gui.py`          | Interfaz gráfica de la aplicación.           |
| `main.py`             | Ejecución y demostración del sistema.        |
| `catalogo.py`         | Gestión del catálogo de equipos.             |
| `equipo.py`           | Modelo y validación de los equipos.          |
| `usuario.py`          | Modelo y validación de usuarios.             |
| `persona.py`          | Información básica de las personas.          |
| `cliente.py`          | Gestión de tipos de cliente y descuentos.    |
| `prestamo.py`         | Gestión de préstamos, devoluciones y multas. |
| `datos_catalogo.json` | Almacenamiento de los datos del catálogo.    |
| `assets/logo.png`     | Logo utilizado en la aplicación.             |

---

