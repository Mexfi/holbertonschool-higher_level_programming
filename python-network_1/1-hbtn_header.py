#!/usr/bin/python3
"""
This script fetches the value of the X-Request-Id header from a URL passed
as an argument and prints it.
"""

import urllib.request
import sys

def fetch_request_id(url):
    """
    Fetches the X-Request-Id header from the response of a GET request to the
    provided URL and prints its value.
    """
    with urllib.request.urlopen(url) as response:
        # Get the value of the 'X-Request-Id' header
        request_id = response.getheader("X-Request-Id")

        # Print the value of the X-Request-Id header
        print(request_id)


if __name__ == "__main__":
    # URL passed as a command line argument
    url = sys.argv[1]

    # Call the function to fetch the request ID
    fetch_request_id(url)
