# 👑 William-The-Reader: Plataforma de OCR con IA

William-The-Reader es una aplicación web completa desarrollada en Python, diseñada para escanear, procesar y extraer texto de imágenes utilizando un motor de Inteligencia Artificial (OCR). Este proyecto demuestra una arquitectura de software modular y la integración de sistemas de IA con una aplicación web funcional.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Características Principales

* **Autenticación de Usuarios:** Sistema completo de registro e inicio de sesión (`login.py`) para gestionar el acceso de usuarios.
* **Procesamiento de Imágenes:** Módulo dedicado (`escanear.py`) para cargar y pre-procesar imágenes antes del análisis.
* **Motor de IA (OCR):** Un núcleo de IA (`ia_lectora.py`) que se encarga de "leer" las imágenes y extraer el texto contenido en ellas.
* **Base de Datos:** Persistencia de datos de usuarios y resultados de escaneo en una base de datos (`database/`).
* **Interfaz Web:** Aplicación web centralizada (`app.py`) que sirve como punto de entrada y conecta todos los módulos.

## 🖼️ Demostración

*[¡RECOMENDADO!] Inserta aquí un GIF o una captura de pantalla de tu aplicación en funcionamiento. Sube la imagen a tu repositorio (ej. en la carpeta `assets`) y usa este enlace:*

`![Demo de William-The-Reader](assets/demo.gif)`

---

## 🛠️ Stack Tecnológico

Este proyecto demuestra competencia en las siguientes tecnologías:

* **Backend:** **Python**
* **Web Framework:** **Flask**
* **IA / OCR:** **[Indica aquí la librería, ej: Tesseract, EasyOCR, OpenCV]** (implementado en `ia_lectora.py`)
* **Base de Datos:** **[Indica aquí la BD, ej: SQLite, PostgreSQL]** (gestionado desde `database/`)
* **Frontend:** HTML5, CSS3, JavaScript (servido desde `assets/`)

---

## 🏗️ Arquitectura del Proyecto

La estructura del código está diseñada para ser modular y escalable, separando las responsabilidades clave:

```text
├── Scripts/            # Scripts de utilidad (ej. inicializar BD)
├── assets/             # Archivos estáticos (CSS, JS, Imágenes)
├── database/           # Almacén de la base de datos (ej. app.db)
├── app.py              # 1. Punto de entrada principal (Flask App)
├── login.py            # 2. Módulo de autenticación y gestión de sesiones
├── escanear.py         # 3. Módulo de carga y procesamiento de imágenes
├── ia_lectora.py       # 4. Módulo de IA (OCR)
└── requirements.txt    # Dependencias del proyecto
```


  **Flujo de trabajo:**

1.  El usuario interactúa con la aplicación principal (`app.py`).
2.  Si el usuario no está autenticado, `app.py` utiliza `login.py` para gestionar el registro o inicio de sesión.
3.  Una vez autenticado, el usuario carga una imagen. `app.py` pasa esta imagen al módulo `escanear.py` para su validación y pre-procesamiento.
4.  La imagen procesada se envía al motor de IA, `ia_lectora.py`, que devuelve el texto extraído.
5.  `app.py` muestra el resultado al usuario.

---
