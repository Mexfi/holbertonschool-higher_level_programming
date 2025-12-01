#!/usr/bin/python3
"""
Python script that takes a URL and an email, sends a POST request
to the URL with the email as a parameter, and displays the response body.
Uses only 'requests' and 'sys' packages.
"""
import requests
import sys


def post_email():
    """
    Sends a POST request to the URL with the email as 'email' parameter.
    """
    # URL is the first command-line argument
    url = sys.argv[1]
    # Email is the second command-line argument
    email_address = sys.argv[2]

    # The data to be sent in the POST request body.
    # The email must be sent in the variable 'email'.
    payload = {'email': email_address}

    # Send the POST request
    try:
        response = requests.post(url, data=payload)

        # Display the body of the response (decoded as a string)
        print(response.text)

    except requests.exceptions.RequestException:
        # Handle connection errors gracefully if necessary
        pass


if __name__ == "__main__":
    post_email()
