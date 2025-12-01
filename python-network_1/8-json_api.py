#!/usr/bin/python3
"""
Python script that takes a letter, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as parameter 'q'.
Handles JSON response, displaying id and name, or error messages.
Uses only 'requests' and 'sys'.
"""
import requests
import sys


def search_user():
    """
    Sends a POST request and processes the JSON response.
    """
    url = "http://0.0.0.0:5000/search_user"

    # Set q value: sys.argv[1] if provided, otherwise empty string
    q = ""
    if len(sys.argv) > 1:
        q = sys.argv[1]

    # Prepare the data payload
    payload = {'q': q}

    try:
        # Send the POST request
        response = requests.post(url, data=payload)

        # Attempt to decode the response body as JSON
        try:
            json_data = response.json()

            # Check if the JSON dictionary is empty
            if not json_data:
                print("No result")
            else:
                # Display the id and name in the required format
                user_id = json_data.get('id')
                user_name = json_data.get('name')
                print(f"[{user_id}] {user_name}")

        except ValueError:
            # Executes if response.json() fails to decode the body
            print("Not a valid JSON")

    except requests.exceptions.RequestException:
        # Handle connection errors (not explicitly required, but good practice)
        pass


if __name__ == "__main__":
    search_user()
