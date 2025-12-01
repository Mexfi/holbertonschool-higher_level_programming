#!/usr/bin/python3
"""
Uses GitHub credentials (username/token) to display user ID via GitHub API.
"""
import requests
import sys


def get_github_id():
    """
    Retrieves the user ID from the GitHub API using Basic Authentication.
    """
    # The first argument is the username
    username = sys.argv[1]
    # The second argument is the Personal Access Token
    token = sys.argv[2]

    # GitHub API endpoint for the authenticated user
    url = "https://api.github.com/user"

    # Use the 'auth' parameter for Basic Authentication: (username, token)
    try:
        response = requests.get(url, auth=(username, token))

        # Check for successful response (Status 200)
        if response.status_code == 200:
            user_data = response.json()
            # Print the 'id' field
            print(user_data.get('id'))
        else:
            # Print "None" for 401 Unauthorized or other errors
            print("None")

    except requests.exceptions.RequestException:
        # Handle connection errors (DNS failure, timeout, etc.)
        print("None")


if __name__ == "__main__":
    get_github_id()
