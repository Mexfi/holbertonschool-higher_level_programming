#!/usr/bin/python3
"""XML serialization and deserialization module"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML file

    Args:
        dictionary (dict): The Python dictionary to serialize
        filename (str): The filename to save the XML data

    Returns:
        None
    """
    # Create root element
    root = ET.Element("data")

    # Iterate through dictionary items and add as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create ElementTree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML file to Python dictionary

    Args:
        filename (str): The filename to read XML data from

    Returns:
        dict: The deserialized Python dictionary
    """
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruct dictionary from XML elements
    result_dict = {}
    for child in root:
        result_dict[child.tag] = child.text

    return result_dict
