#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays
the body of the response (decoded in utf-8).
It must manage urllib.error.HTTPError exceptions and print the error code.
Usage: ./3-error_code.py <URL>
"""
import urllib.request
import urllib.error
import sys

# The URL is passed as the first command-line argument
url = sys.argv[1]

try:
    # Use the 'with' statement for proper resource management
    with urllib.request.urlopen(url) as response:
        # Read the body and decode it using utf-8
        body = response.read().decode('utf-8')
        print(body)

# Catch the specific HTTPError exception
except urllib.error.HTTPError as e:
    # If an HTTPError occurs, print the specific error code
    print(f"Error code: {e.code}")
