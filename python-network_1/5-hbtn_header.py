#!/usr/bin/python3
import sys
import requests

if __name__ == "__main__":
    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Extract and print the value of the 'X-Request-Id' header
    print(response.headers.get('X-Request-Id'))
