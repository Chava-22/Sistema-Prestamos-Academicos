# Sistema de Préstamos Académicos

**Nombre:** Andrés Calderón
**Universidad:** Universidad de Especialidades Espíritu Santo (UEES)
**Carrera:** Ingeniería en Desarrollo, Operación y Seguridad de Software

## Descripción del proyecto

El **Sistema de Préstamos Académicos** es una aplicación desarrollada en Python para gestionar equipos académicos como laptops, proyectores y tablets. El sistema permite registrar, buscar, actualizar y eliminar equipos, controlar su disponibilidad y gestionar préstamos.

El proyecto cuenta con un catálogo de productos que utiliza diferentes estructuras de datos para organizar la información y evitar registros duplicados. También incorpora una fila de espera para gestionar solicitudes cuando un equipo se encuentra prestado, respetando el principio **FIFO (First In, First Out)**.

La información se almacena mediante el patrón **Repository**, separando la lógica del sistema de la lectura y escritura de archivos. Además, se utiliza **Pydantic** para validar automáticamente los datos ingresados.

El proyecto incluye una **interfaz gráfica** desarrollada con Flet, desde la cual se pueden administrar los equipos y visualizar su estado. También cuenta con **pruebas unitarias automatizadas mediante pytest** para comprobar el correcto funcionamiento de las principales funcionalidades del sistema.

## Instrucciones para ejecutar el proyecto

### 1. Abrir el proyecto

Abrir el archivo:

```text
SistemaPrestamosAcademicos.slnx
```

utilizando **Visual Studio Community**.

### 2. Instalar las dependencias

Abrir una terminal dentro de Visual Studio y ejecutar:

```bash
pip install pydantic flet pytest
```

### 3. Ejecutar el programa por consola

Para ejecutar la demostración principal del sistema:

```bash
python main.py
```

### 4. Ejecutar la interfaz gráfica

Para abrir la aplicación gráfica:

```bash
python app_gui.py
```

## Instrucciones para ejecutar las pruebas unitarias

Las pruebas unitarias se encuentran dentro de la carpeta:

```text
tests/
```

Para ejecutarlas, abrir una terminal en la carpeta principal del proyecto y ejecutar:

```bash
pytest
```

También se pueden ejecutar mediante:

```bash
python -m pytest
```

Las pruebas verifican el correcto funcionamiento de funcionalidades como:

* El orden de atención de la fila de espera.
* El comportamiento de la cola cuando está vacía.
* La conservación de los datos después de cerrar y volver a abrir el sistema.
* El control de productos duplicados en el catálogo.
* El funcionamiento de las principales reglas de negocio del sistema.

Si todas las pruebas se ejecutan correctamente, **pytest** mostrará el resultado indicando que las pruebas fueron superadas.
