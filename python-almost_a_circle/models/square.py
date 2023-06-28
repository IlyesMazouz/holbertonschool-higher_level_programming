#!/usr/bin/python3
"""
creating the square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method
        Args:
            size (int): Size of the square
            x (int): x-coordinate of the square's position (default 0)
            y (int): y-coordinate of the square's position (default 0)
            id (int): Identifier of the square (default None)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square
        Returns:
            str: String representation of the Square object
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value
