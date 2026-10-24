#!/usr/bin/env python3
"""Módulo para escribir texto en un archivo."""


def write_file(filename="", text=""):
    """Escribe una cadena en un archivo y dev. el n. de caract."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
