#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """
    BaseGeometry class representing a base geometry shape.
    """

    def area(self):
        """
        Calculate the area of the geometry shape.
        This method should be overridden by subclasses.
        :return: None
        :raises: Exception with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the given value as an integer based on the provided rules.
        :param name: The name of the value as a string.
        :param value: The value to be validated.
        :return: None
        :raises:
            - TypeError if value is not an integer
              with the message "<name> must be an integer"
            - ValueError if value is less than or equal to 0
              with the message "<name> must be greater than 0"
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")