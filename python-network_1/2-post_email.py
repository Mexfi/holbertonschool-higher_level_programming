#!/usr/bin/python3
"""
This script sends a POST request to a URL with the email as a parameter and
prints the body of the response decoded in UTF-8.
"""

import urllib.parse
import urllib.request
import sys


def send_email_post(url, email):
    """
    Sends a POST request to the specified URL with the email as a parameter
    and prints the decoded body of the response.
    """
    # Prepare the data to be sent in the POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send the POST request with the email as the parameter
    with urllib.request.urlopen(url, data) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')

        # Print the body of the response
        print(body)


if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Call the function to send the POST request and print the response
    send_email_post(url, email)
