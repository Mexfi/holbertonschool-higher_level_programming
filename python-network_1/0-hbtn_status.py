#!/usr/bin/python3
import urllib.request

"""
This script fetches the status of https://intranet.hbtn.io/status
and displays the response body in a specific format.
"""
def fetch_status():
    url = "https://intranet.hbtn.io/status"

    # Use a with statement to fetch the URL
    with urllib.request.urlopen(url) as response:
        body = response.read()

        # Print the body response as required
        print("Body response:")
        print(f"    - type: {type(body)}")
        print(f"    - content: {body}")
        print(f"    - utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()
