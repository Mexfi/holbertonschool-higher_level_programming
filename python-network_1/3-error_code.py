#!/usr/bin/python3
"""
Takes in a URL, sends a request to it, and displays the body of the response
(decoded in utf-8). It manages urllib.error.HTTPError exceptions and
prints the HTTP status code on failure.
"""
import urllib.request
import urllib.error
import sys


def fetch_url_body(url):
    """
    Sends a request to the given URL and prints the response body.
    Handles HTTPError exceptions.

    Args:
        url (str): The URL to request.
    """
    try:
        # Use 'with' statement for proper resource management
        with urllib.request.urlopen(url) as response:
            # Read the body and decode it using utf-8
            body = response.read().decode('utf-8')
            print(body)
    # Catch the specific HTTPError exception
    except urllib.error.HTTPError as e:
        # If an HTTPError occurs, print the specific error code
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    # The URL is passed as the first command-line argument
    if len(sys.argv) > 1:
        fetch_url_body(sys.argv[1])
