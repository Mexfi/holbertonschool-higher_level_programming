#!/usr/bin/python3
import urllib.request

"""
This script fetches the status of https://intranet.hbtn.io/status
(or any URL passed as a constant) and displays the response body in a specific format.
"""

def fetch_status():
    """
    Fetches and displays the status of the URL.
    The script fetches the body of the response and prints it in the following format:
    - type: <type of content>
    - content: <raw content of the response>
    - utf8 content: <decoded utf-8 content of the response>
    """
    url = "https://intranet.hbtn.io/status"  # Default URL

    # You can change the URL to test it for different environments
    # url = "http://0.0.0.0:5050/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()

        # Print the body response in the required format
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()
