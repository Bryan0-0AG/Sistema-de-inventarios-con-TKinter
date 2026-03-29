# 📦 Sistema de Inventarios con Tkinter

> Aplicación de escritorio en Python para gestionar inventarios de productos con interfaz gráfica, persistencia en Excel y visualización de datos en tiempo real.

---

## 📋 Descripción

Este proyecto es un **sistema de gestión de inventarios** desarrollado en Python, que combina una interfaz gráfica construida con **Tkinter** y almacenamiento de datos en archivos **Excel** mediante **pandas**. Permite añadir, eliminar, actualizar y restar productos de un inventario, reflejando los cambios de forma inmediata en una ventana de visualización secundaria.

El proyecto está orientado al aprendizaje práctico de la programación orientada a objetos, el manejo de archivos con pandas y el desarrollo de interfaces de usuario con Tkinter.

---

## 🗂️ Estructura del proyecto

```
Sistema-de-inventarios-con-TKinter/
│
├── Main.py                    # Lógica del inventario (clases y operaciones CRUD)
├── Interfaz.py                # Interfaz gráfica principal con Tkinter
├── Visualización_deDatos.py   # Ventana secundaria de visualización en tiempo real
├── .gitignore                 # Archivos ignorados por Git
└── LICENSE                    # Licencia MIT
```

> Los inventarios se guardan automáticamente en una carpeta `Inventarios/` que se crea en el mismo directorio del proyecto.

---

## ⚙️ Funcionalidades

- **Añadir producto** — Registra un nuevo producto con nombre, precio y cantidad. Si ya existe, suma la cantidad indicada.
- **Restar producto** — Reduce la cantidad de un producto existente. Si la cantidad a restar supera el stock, solicita confirmación antes de proceder.
- **Eliminar producto** — Borra completamente un producto del inventario.
- **Actualizar cantidad** — Modifica directamente la cantidad de un producto existente.
- **Actualizar precio** — Modifica el precio de un producto sin alterar su stock.
- **Visualización en tiempo real** — Una ventana secundaria muestra la tabla del inventario (nombre, precio, cantidad) y se actualiza automáticamente tras cada operación.
- **Persistencia en Excel** — Todos los datos se guardan en un archivo `.xlsx` dentro de la carpeta `Inventarios/`, conservando el estado entre ejecuciones.

---

## 🖥️ Interfaz gráfica

La aplicación abre **dos ventanas simultáneas**:

| Ventana | Descripción |
|---|---|
| **Ventana principal** (`Interfaz.py`) | Formulario con campos de nombre, precio y cantidad, más botones para cada operación. |
| **Ventana de datos** (`Visualización_deDatos.py`) | Tabla en tiempo real con todos los productos del inventario activo. |

---

## 🚀 Instalación y uso

### Requisitos

- Python 3.8+
- Las siguientes librerías:

```bash
pip install pandas openpyxl
```

> `tkinter` viene incluido por defecto en la instalación estándar de Python.

### Ejecutar la aplicación

```bash
python Interfaz.py
```

Esto abrirá la ventana principal de gestión y la ventana de visualización de datos de forma automática.

---

## 🧱 Arquitectura del código

El proyecto sigue un enfoque orientado a objetos, separando responsabilidades en tres módulos:

**`Main.py`** define dos clases principales:
- `nuevo_producto` — Representa un producto con nombre y precio.
- `nuevo_inventario` — Gestiona el archivo Excel y expone los métodos CRUD del inventario.

**`Interfaz.py`** construye la GUI con Tkinter, instancia el inventario y conecta cada botón a la acción correspondiente, llamando también a la actualización visual tras cada operación.

**`Visualización_deDatos.py`** mantiene una segunda ventana Tkinter que lee el Excel y reconstruye la tabla de productos cada vez que se invoca `actualizar_visualizacion_datos()`.

---

## 🛠️ Tecnologías utilizadas

- **Python** — Lenguaje principal
- **Tkinter** — Interfaz gráfica de escritorio
- **pandas** — Lectura y escritura de datos en Excel
- **openpyxl** — Motor de soporte para archivos `.xlsx`

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

## 👤 Autor

**Bryan0-0AG**  
Proyecto personal para aprender Python, POO e interfaces gráficas de escritorio.
