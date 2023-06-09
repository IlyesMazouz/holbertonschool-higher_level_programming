#!/usr/bin/python3
"""
Defines a Rectangle class that represents a rectangle
"""


class Rectangle:
    """
    Class that represents a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance

        Args:
            width (int): The width of the rectangle. Defaults to 0
            height (int): The height of the rectangle. Defaults to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle

        Returns:
            int: The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): The width value to set

        Raises:
            TypeError: If the width is not an integer
            ValueError: If the width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle

        Returns:
            int: The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value (int): The height value to set

        Raises:
            TypeError: If the height is not an integer
            ValueError: If the height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            str: The string representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return (symbol * self.__width + "\n") * self.__height

    def __repr__(self):
        """
        Returns a string representation of the rectangle that
        can be used to recreate a new instance

        Returns:
            str: The string representation of the rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a farewell message when the rectangle instance is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles based on their areas and
        returns the rectangle with the greater or equal area

        Args:
            rect_1 (Rectangle): The first rectangle to compare
            rect_2 (Rectangle): The second rectangle to compare

        Returns:
            Rectangle: The rectangle with the greater or equal area

        Raises:
           TypeError: If rect_1 is not an instance of Rectangle
            TypeError: If rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new Rectangle instance with equal width and height

        Args:
            size (int): The size of the square. Defaults to 0

        Returns:
            Rectangle: A new Rectangle instance representing a square
        """
        return cls(size, size)
