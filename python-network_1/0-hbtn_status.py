#!/usr/bin/python3
"""
This module fetches the status of a given URL using urllib and prints the
response body in a specific format required by the project.
"""

import urllib.request


def fetch_status():
    """
    Fetches https://intranet.hbtn.io/status and prints the body in the required
    format. It includes the cfclearance header to bypass firewall filtering.
    """
    url = "https://intranet.hbtn.io/status"

    req = urllib.request.Request(
        url,
        headers={'cfclearance': 'true'}
    )

    with urllib.request.urlopen(req) as response:
        body = response.read()

        print("Body response:")
        print("    - type: {}".format(type(body)))
        print("    - content: {}".format(body))
        print("    - utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    fetch_status()
