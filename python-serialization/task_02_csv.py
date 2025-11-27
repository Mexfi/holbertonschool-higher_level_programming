#!/usr/bin/python3
"""CSV to JSON conversion module"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file to JSON format

    Args:
        csv_filename (str): The filename of the input CSV file

    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        # Read data from CSV file
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        # Serialize data to JSON and write to file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        return False
    except Exception:
        return False
