# 👑 William-The-Reader:
## (EN)
William-The-Reader is a comprehensive desktop application developed in Python, designed to read scanned, processed, and extracted text from images using OCR. This project showcases a modular software architecture and the integration of AI systems with a functional TKinter application.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![UI](https://img.shields.io/badge/UI-Tkinter-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![OCR](https://img.shields.io/badge/OCR-EasyOCR-green.svg)](https://github.com/JaidedAI/EasyOCR)
[![TTS](https://img.shields.io/badge/TTS-ElevenLabs-blueviolet.svg)](https://elevenlabs.io/)
[![Database](https://img.shields.io/badge/Database-SQLite-informational.svg)](https://www.sqlite.org/index.html)

---

## 🌟 Key Features

* **User Authentication:** Complete registration and login system (`login.py`) to manage user access.
* **Image Processing:** Dedicated module (`escanear.py`) for uploading and processing images into text.
* **AI Engine (Eleven Labs):** An AI core (`ia_lectora.py`) responsible for "reading" the text from images or from direct app input.
* **Database:** Data persistence for user data and scan results in a database (`database/`).
* **Interface:** Centralized application (`app.py`) that serves as the entry point and connects all modules.

## 🖼️ Demonstration
<img width="1238" height="649" alt="image" src="https://github.com/user-attachments/assets/96b1808d-fe39-4725-8985-e3c350e849ea" />

<img width="1230" height="639" alt="image" src="https://github.com/user-attachments/assets/d99c8028-3b30-450f-983e-8e45230c0353" />

<img width="1586" height="795" alt="image" src="https://github.com/user-attachments/assets/f883f684-a6d0-4c85-a8ef-6f6df9144bd1" />

---

## 🛠️ Tech Stack

This project demonstrates proficiency in the following technologies:

* **Backend:** **Python**
* **AI / OCR:** **easyocr** (implemented in `ia_lectora.py`)
* **Database:** **SQLite** (managed from `database/`)
* **Frontend:** **TKinter** (with assets from `assets/`)

---

## 🏗️ Project Architecture

The code structure is designed to be modular and scalable, separating key responsibilities:

```text
├── assets/         Static files (Images or audio)
├── database/       Database storage (e.g., app.db)
├── app.py          1. Main entry point (TKinter App)
├── login.py        2. Authentication and session management module
├── escanear.py     3. Image upload and processing module (easyocr)
├── ia_lectora.py   4. AI module
└── requirements.txt  Project dependencies
```


# 👑 William-The-Reader:
## (ES)
William-The-Reader es una aplicación de escritorio completa desarrollada en Python, diseñada para leer texto escaneado, procesado y extraido de imágenes utilizando OCR. Este proyecto demuestra una arquitectura de software modular y la integración de sistemas de IA con una aplicación TKinter funcional.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![UI](https://img.shields.io/badge/UI-Tkinter-orange.svg)](https://docs.python.org/3/library/tkinter.html)
[![OCR](https://img.shields.io/badge/OCR-EasyOCR-green.svg)](https://github.com/JaidedAI/EasyOCR)
[![TTS](https://img.shields.io/badge/TTS-ElevenLabs-blueviolet.svg)](https://elevenlabs.io/)
[![Database](https://img.shields.io/badge/Database-SQLite-informational.svg)](https://www.sqlite.org/index.html)

---

## 🌟 Características Principales

* **Autenticación de Usuarios:** Sistema completo de registro e inicio de sesión (`login.py`) para gestionar el acceso de usuarios.
* **Procesamiento de Imágenes:** Módulo dedicado (`escanear.py`) para cargar y procesar imágenes a texto.
* **Motor de IA (Eleven Labs):** Un núcleo de IA (`ia_lectora.py`) que se encarga de "leer" el texto de las imagenes o del propio input de la App.
* **Base de Datos:** Persistencia de datos de usuarios y resultados de escaneo en una base de datos (`database/`).
* **Interfaz:** Aplicación centralizada (`app.py`) que sirve como punto de entrada y conecta todos los módulos.

## 🖼️ Demostración
<img width="1238" height="649" alt="image" src="https://github.com/user-attachments/assets/96b1808d-fe39-4725-8985-e3c350e849ea" />

<img width="1230" height="639" alt="image" src="https://github.com/user-attachments/assets/d99c8028-3b30-450f-983e-8e45230c0353" />

<img width="1586" height="795" alt="image" src="https://github.com/user-attachments/assets/f883f684-a6d0-4c85-a8ef-6f6df9144bd1" />


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
├── assets/             Archivos estáticos (Imágenes o audios)
├── database/           Almacén de la base de datos (ej. app.db)
├── app.py              1. Punto de entrada principal (TKinter App)
├── login.py            2. Módulo de autenticación y gestión de sesiones
├── escanear.py         3. Módulo de carga y procesamiento de imágenes (easyocr)
├── ia_lectora.py       4. Módulo de IA 
└── requirements.txt    Dependencias del proyecto
```


  **Flujo de trabajo:**

1.  El usuario interactúa con la aplicación principal (`app.py`).
2.  Si el usuario no está autenticado, `app.py` utiliza `login.py` para gestionar el registro o inicio de sesión.
3.  Una vez autenticado, el usuario carga una imagen o inserta un texto. En el caso de que sea imagen`app.py` pasa la imagen al módulo `escanear.py` para pasar todo el texto de la imagen.
4.  La imagen procesada o el texto se envía al motor de IA, `ia_lectora.py`, que crea un audio con voz real humana (Utilizando Eleven Labs).
5.  `app.py` abre este mp3 y lo ejecuta.

---
