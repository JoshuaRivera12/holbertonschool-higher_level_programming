#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def pos_print(self):
        s_position = ""
        if self.size == 0:
            return "\n"

        for n in range(self.position[1]):
            s_position += "\n"

        for n in range(self.size):
            for x in range(self.position[0]):
                s_position += " "

            for y in range(self.size):
                s_position += "#"

            s_position += "\n"

        return s_position

    def __str__(self):
        return self.pos_print()
