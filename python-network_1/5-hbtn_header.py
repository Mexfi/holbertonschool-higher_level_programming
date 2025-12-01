#!/usr/bin/python3
"""
This script takes in a URL, sends a GET request to the URL, and displays the
value of the 'X-Request-Id' variable in the response header. If the 'X-Request-Id'
is not present, it does not output anything.
"""

import sys
import requests


def fetch_request_id(url):
    """
    Fetch the 'X-Request-Id' from the response header after sending a GET request
    to the given URL. Handles redirection and missing headers.
    """
    response = requests.get(url, allow_redirects=True)

    # Get the 'X-Request-Id' header, if it exists
    request_id = response.headers.get('X-Request-Id')

    if request_id:
        print(request_id)


if __name__ == "__main__":
    # URL passed as a command-line argument
    url = sys.argv[1]

    # Call the function to fetch and print the 'X-Request-Id'
    fetch_request_id(url)
