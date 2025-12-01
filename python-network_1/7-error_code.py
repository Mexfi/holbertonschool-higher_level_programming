#!/usr/bin/python3
"""
Python script that takes a URL, sends a request, and displays the response body.
If the HTTP status code is 400 or greater, it prints an error code message.
Uses only 'requests' and 'sys' packages.
"""
import requests
import sys


def check_url_status():
    """
    Sends a GET request to the URL provided as a command-line argument.
    Prints the body if the status code is < 400, or prints an error message
    if the status code is >= 400.
    """
    # The URL is the first command-line argument
    url = sys.argv[1]

    try:
        # Send a GET request
        response = requests.get(url)

        # Check the HTTP status code
        if response.status_code >= 400:
            # If the status code indicates an error (4xx or 5xx)
            print(f"Error code: {response.status_code}")
        else:
            # Display the body of the response for success codes (< 400)
            print(response.text)

    except requests.exceptions.RequestException:
        # Handle connection errors (DNS failure, timeout, etc.) gracefully.
        # Although not explicitly required, this prevents the script from crashing.
        pass


if __name__ == "__main__":
    check_url_status()
