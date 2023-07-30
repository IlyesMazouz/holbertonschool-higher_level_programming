#!/usr/bin/python3
"""
a Student class that defines a student
"""


class Student:
    """
    Defines a student by their first_name, last_name, and age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given attributes

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list, optional):
              A list of strings specifying the attribute names
            to be included in the dictionary representation
            If None, all attributes are included

        Returns:
            dict: A dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
            return student_dict
