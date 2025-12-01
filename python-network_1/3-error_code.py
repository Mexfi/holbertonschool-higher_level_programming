#!/usr/bin/python3
"""
This script sends a GET request to a URL and displays the body of the response
(decoded in UTF-8). If an HTTP error occurs, it prints "Error code: <HTTP status 
code>".
"""

import urllib.request
import sys
import urllib.error


def fetch_url(url):
    """
    Fetches the URL and handles HTTPError exceptions by printing the error code.
    If successful, it prints the body of the response in UTF-8.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)

    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Call the function to fetch the URL and handle errors
    fetch_url(url)
