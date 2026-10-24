#!/usr/bin/env python3
"""Módulo que contiene una función para leer archivos de texto en formato UTF-8."""

def read_file(filename=""):
    """Lee un archivo de texto en codificación UTF-8 y lo imprime en la salida estándar."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
