#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
and displays the body of the response in a specific format.
"""
import requests


def fetch_hbtn_status():
    """
    Fetches the status page and prints information about the content.
    """
    url = "https://intranet.hbtn.io/status"

    # Send a GET request to the URL
    response = requests.get(url)

    # The content is a bytes object, but the requirement suggests
    # printing the decoded string content.
    content = response.text

    # Print the output in the required format
    print("Body response:")
    # Print the type of the content (which is 'str' after response.text)
    print(f"\t- type: {type(content)}")
    # Print the actual content
    print(f"\t- content: {content}")


if __name__ == "__main__":
    fetch_hbtn_status()
