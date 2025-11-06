# 👑 William-The-Reader: Plataforma de OCR con IA

William-The-Reader es una aplicación web completa desarrollada en Python, diseñada para escanear, procesar y extraer texto de imágenes utilizando un motor de Inteligencia Artificial (OCR). Este proyecto demuestra una arquitectura de software modular y la integración de sistemas de IA con una aplicación web funcional.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Flask-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](https://opensource.org/licenses/MIT)

---

## 🌟 Características Principales

* **Autenticación de Usuarios:** Sistema completo de registro e inicio de sesión (`login.py`) para gestionar el acceso de usuarios.
* **Procesamiento de Imágenes:** Módulo dedicado (`escanear.py`) para cargar y procesar imágenes a texto.
* **Motor de IA (Eleven Labs):** Un núcleo de IA (`ia_lectora.py`) que se encarga de "leer" el texto de las imagenes o del propio input de la App.
* **Base de Datos:** Persistencia de datos de usuarios y resultados de escaneo en una base de datos (`database/`).
* **Interfaz:** Aplicación centralizada (`app.py`) que sirve como punto de entrada y conecta todos los módulos.

## 🖼️ Demostración


---

## 🛠️ Stack Tecnológico

Este proyecto demuestra competencia en las siguientes tecnologías:

* **Backend:** **Python**
* **IA / OCR:** **easyocr** (implementado en `ia_lectora.py`)
* **Base de Datos:** **SQLite** (gestionado desde `database/`)
* **Frontend:** TKinter (servido desde `assets/`)

---

## 🏗️ Arquitectura del Proyecto

La estructura del código está diseñada para ser modular y escalable, separando las responsabilidades clave:

```text
├── assets/             # Archivos estáticos (Imágenes o audios)
├── database/           # Almacén de la base de datos (ej. app.db)
├── app.py              # 1. Punto de entrada principal (TKinter App)
├── login.py            # 2. Módulo de autenticación y gestión de sesiones
├── escanear.py         # 3. Módulo de carga y procesamiento de imágenes (easyocr)
├── ia_lectora.py       # 4. Módulo de IA 
└── requirements.txt    # Dependencias del proyecto
```


  **Flujo de trabajo:**

1.  El usuario interactúa con la aplicación principal (`app.py`).
2.  Si el usuario no está autenticado, `app.py` utiliza `login.py` para gestionar el registro o inicio de sesión.
3.  Una vez autenticado, el usuario carga una imagen o inserta un texto. En el caso de que sea imagen`app.py` pasa la imagen al módulo `escanear.py` para pasar todo el texto de la imagen.
4.  La imagen procesada o el texto se envía al motor de IA, `ia_lectora.py`, que crea un audio con voz real humana (Utilizando Eleven Labs).
5.  `app.py` abre este mp3 y lo ejecuta.

---
