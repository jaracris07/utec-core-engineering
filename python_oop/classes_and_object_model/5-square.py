#!/usr/bin/env python3
"""Módulo que define una clase Square con tamaño,
validación, área, getters/setters y método de impresión.
"""


class Square:
    """Clase que representa un cuadrado con
    tamaño validado, área y método para imprimirlo.
    """

    def __init__(self, size=0):
        """Inicializa un cuadrado con tamaño opcional."""
        self.size = size

    @property
    def size(self):
        """Recupera el valor actual del tamaño."""
        return self.__size

    @size.setter
    def size(self, value):
        """Establece y valida un nuevo valor para el tamaño."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Devuelve el área actual del cuadrado."""
        return self.__size ** 2

    def my_print(self):
        """Imprime en la salida estándar el cuadrado con el carácter #."""
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
