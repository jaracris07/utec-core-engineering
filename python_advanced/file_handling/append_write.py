#!/usr/bin/env python3
"""Módulo para añadir texto al final de un archivo."""


def append_write(filename="", text=""):
    """Añade texto al final de un archivo y devuelvelos caract. añadidos."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
