#!/usr/bin/python3
"""Custom object serialization using pickle"""

import pickle


class CustomObject:
    """A custom Python class for serialization demonstration"""

    def __init__(self, name, age, is_student):
        """Initialize CustomObject with name, age, and is_student attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in the required format"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save to file

        Args:
            filename (str): The filename to save the serialized object

        Returns:
            None: Returns None if serialization fails
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from file

        Args:
            filename (str): The filename to load the serialized object from

        Returns:
            CustomObject or None: Returns deserialized object or None if deserialization fails
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
