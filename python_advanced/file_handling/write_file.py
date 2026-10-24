#!/usr/bin/env python3
"""Módulo para escribir texto en un archivo."""


def write_file(filename="", text=""):
    """Escribe una cadena en un archivo UTF-8 y retorna el número de caracteres."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
