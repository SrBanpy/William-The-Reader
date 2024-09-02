
from elevenlabs import generate,play, set_api_key, save,voices
import os
import requests
import pygame
from pathlib import Path

def leer(texto):
    def reproducir_audio(ruta_archivo):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(ruta_archivo)
        pygame.mixer.music.set_volume(0.35)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()

    set_api_key("acca01bc0e1658a03b3e681c910a1cf8")

    audio = generate(
        text=texto,
        voice="VqtVKa0zif0um10L5WPM",
        model='eleven_multilingual_v1',


    )
    save(audio,"assets\\read.mp3")
    reproducir_audio("assets\\read.mp3")

def guardar_audio_ia(texto,nombre):

    set_api_key("acca01bc0e1658a03b3e681c910a1cf8")

    audio = generate(
        text=texto,
        voice="VqtVKa0zif0um10L5WPM",
        model='eleven_multilingual_v1',


    )
    save(audio,nombre)