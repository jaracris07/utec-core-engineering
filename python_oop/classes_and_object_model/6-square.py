#!/usr/bin/env python3
"""Módulo que define una clase Square con tamaño,
posición, validación, getters/setters, área e impresión.
"""


class Square:
    """Clase que representa un cuadrado con
    tamaño, posición y métodos de impresión.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Inicializa un cuadrado con tamaño y posición opcionales."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Recupera la posición actual del cuadrado."""
        return self.__position

    @position.setter
    def position(self, value):
        """Establece y valida una nueva posición para el cuadrado."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        if value[0] < 0 or value[1] < 0:
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value

    def area(self):
        """Devuelve el área actual del cuadrado."""
        return self.__size ** 2

    def __str__(self):
        """Define la representación en cadena de la instancia."""
        if self.__size == 0:
            return ""

        result = []
        for _ in range(self.__position[1]):
            result.append("")

        for _ in range(self.__size):
            spaces = " " * self.__position[0]
            hashes = "#" * self.__size
            result.append(spaces + hashes)

        return "\n".join(result)

    def my_print(self):
        """Imprime en la salida estándar el cuadrado usando __str__."""
        print(self)
        