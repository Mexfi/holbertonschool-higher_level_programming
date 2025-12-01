#!/usr/bin/python3
"""
Takes URL, requests it, and displays the response body or an error code.
Uses 'requests' and 'sys'.
"""
import requests
import sys


def check_url_status():
    """
    Sends GET request and prints body or error code >= 400.
    """
    # URL is the first command-line argument
    url = sys.argv[1]

    try:
        response = requests.get(url)

        # Check the HTTP status code
        if response.status_code >= 400:
            # Print error message for 4xx or 5xx status codes
            print(f"Error code: {response.status_code}")
        else:
            # Display the body for success codes (< 400)
            print(response.text)

    except requests.exceptions.RequestException:
        # Handle connection errors gracefully
        pass


if __name__ == "__main__":
    check_url_status()
