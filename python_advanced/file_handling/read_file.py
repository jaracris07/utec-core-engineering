#!/usr/bin/env python3
"""Módulo para leer archivos."""


def read_file(filename=""):
    """Lee un archivo UTF-8 y lo imprime."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
