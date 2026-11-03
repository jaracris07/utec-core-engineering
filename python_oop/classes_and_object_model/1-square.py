#!/usr/bin/env python3
"""Módulo que define una clase Square con tamaño privado."""


class Square:
    """Clase que representa un cuadrado con tamaño."""

    def __init__(self, size):
        """Inicializa un cuadrado con un tamaño privado."""
        self.__size = size
