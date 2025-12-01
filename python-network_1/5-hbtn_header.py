#!/usr/bin/python3
"""
Takes URL, requests it, and displays X-Request-Id header value.
Uses 'requests' and 'sys'.
"""
import requests
import sys


def get_request_id():
    """Fetches URL from args and prints 'X-Request-Id' from header."""
    if len(sys.argv) < 2:
        return

    url = sys.argv[1]

    try:
        # Send a GET request.
        response = requests.get(url)

        # Retrieve X-Request-Id header value
        x_request_id = response.headers.get(
            'X-Request-Id'
        )

        if x_request_id:
            print(x_request_id)

    except requests.exceptions.RequestException:
        pass


if __name__ == "__main__":
    get_request_id()
