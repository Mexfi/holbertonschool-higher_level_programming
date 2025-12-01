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
    # Check if a URL argument was provided (though the requirement says not to check)
    if len(sys.argv) < 2:
        return

    url = sys.argv[1]

    try:
        # Send a GET request. requests automatically follows redirects (301, 302, etc.).
        # The headers checked will be from the final response, which covers the
        # "one redirection" case correctly.
        response = requests.get(url)

        # Access the headers dictionary and safely get the 'X-Request-Id' value.
        x_request_id = response.headers.get('X-Request-Id')

        # Print the value of the header if it exists
        if x_request_id:
            print(x_request_id)

    except requests.exceptions.RequestException:
        # Catch network/connection errors, but do nothing (pass) as per typical requirements.
        pass


if __name__ == "__main__":
    get_request_id()
