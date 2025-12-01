#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to it, and displays
the value of the X-Request-Id variable found in the response header.
Uses only the 'requests' and 'sys' packages.
"""
import requests
import sys


def get_request_id():
    """
    Fetches the URL provided as the first command-line argument and prints the
    value of the 'X-Request-Id' header from the response.
    """
    # Get the URL from the first command-line argument (sys.argv[1])
    # No need for argument checking as per the requirement.
    url = sys.argv[1]

    # Send a GET request to the URL. The requests library automatically
    # handles the HTTP connection and response.
    try:
        response = requests.get(url)

        # Access the headers dictionary. The .headers attribute is a
        # case-insensitive dictionary-like object. We use .get() for
        # safety, although 'requests' usually normalizes header names.
        x_request_id = response.headers.get('X-Request-Id')

        # Print the value of the header if it exists
        if x_request_id:
            print(x_request_id)

    except requests.exceptions.RequestException:
        # Silently handle errors like network failures or bad URLs,
        # as the focus is only on displaying the header on success.
        pass


if __name__ == "__main__":
    get_request_id()
