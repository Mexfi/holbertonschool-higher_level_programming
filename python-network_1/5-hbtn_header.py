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
    # Check if a URL argument was provided
    if len(sys.argv) < 2:
        return

    url = sys.argv[1]

    # Send a GET request to the URL.
    # requests follows redirects by default, and 'response' will contain
    # the final destination's headers.
    try:
        response = requests.get(url)

        # Access the headers dictionary and use the .get() method to safely
        # retrieve the value of 'X-Request-Id'.
        x_request_id = response.headers.get('X-Request-Id')

        # Print the value if it exists
        if x_request_id:
            print(x_request_id)

    except requests.exceptions.RequestException as e:
        # This handles network errors, DNS failures, timeouts, etc.
        # While not strictly required by the prompt, it makes the script more robust.
        # print(f"An error occurred: {e}", file=sys.stderr)
        pass  # Do nothing on error as the prompt only focuses on the header


if __name__ == "__main__":
    get_request_id()
