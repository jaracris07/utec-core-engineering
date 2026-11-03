#!/usr/bin/env python3
"""Módulo que define una clase Square
con validación de tamaño y cálculo de área.
"""


class Square:
    """Clase que representa un cuadrado con tamaño validado y área."""

    def __init__(self, size=0):
        """Inicializa un cuadrado con un tamaño opcional validado."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Devuelve el área actual del cuadrado."""
        return self.__size ** 2
