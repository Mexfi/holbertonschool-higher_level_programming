#!/usr/bin/python3
"""Basic serialization module"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save data to the specified file"""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize data from the specified file"""
    with open(filename, 'r') as file:
        return json.load(file)
