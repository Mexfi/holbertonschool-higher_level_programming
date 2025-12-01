#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to it, and displays
the value of the X-Request-Id variable found in the response header.
"""
import requests
import sys


def get_request_id():
    """
    Fetches the URL provided as a command-line argument and prints the
    value of the 'X-Request-Id' header from the response.
    """
    # The URL is the first command-line argument
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Access the headers dictionary and use the .get() method to safely
    # retrieve the value of 'X-Request-Id'.
    # .get() is case-insensitive in requests for header keys.
    x_request_id = response.headers.get('X-Request-Id')

    # Print the value
    if x_request_id:
        print(x_request_id)


if __name__ == "__main__":
    get_request_id()
