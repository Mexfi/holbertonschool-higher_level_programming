#!/usr/bin/python3
"""
Python script that takes GitHub credentials (username and Personal Access Token),
uses Basic Authentication with the GitHub API to display the user's ID.
Uses only 'requests' and 'sys'.
"""
import requests
import sys


def get_github_id():
    """
    Retrieves the user ID from the GitHub API using Basic Authentication.
    """
    # The first argument is the username
    username = sys.argv[1]
    # The second argument is the Personal Access Token (used as password)
    token = sys.argv[2]

    # GitHub API endpoint to get the authenticated user's information
    url = "https://api.github.com/user"

    # Use the 'auth' parameter in requests for Basic Authentication.
    # It takes a tuple: (username, password/token)
    try:
        response = requests.get(url, auth=(username, token))

        # Check for successful response (Status 200)
        if response.status_code == 200:
            # The response body is JSON, containing the user details
            user_data = response.json()
            # Extract and print the 'id' field
            print(user_data.get('id'))
        else:
            # For 401 Unauthorized (wrong token/credentials) or other errors
            print("None")

    except requests.exceptions.RequestException:
        # Handle connection errors
        print("None")


if __name__ == "__main__":
    get_github_id()
