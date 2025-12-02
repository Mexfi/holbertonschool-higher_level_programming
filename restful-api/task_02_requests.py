# task_02_requests.py

import requests

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()

        # Iterate through the posts and print out the titles
        for post in posts:
            print(post['title'])
    else:
        print("Failed to retrieve data")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()

        # Prepare the list of dictionaries for CSV writing
        post_data = [{"id": post['id'], "title": post['title'], "body": post['body']} for post in posts]

        # Import CSV module to write data into CSV
        import csv
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()  # Write the header row
            writer.writerows(post_data)  # Write the data rows
        print("Data saved to posts.csv")
    else:
        print("Failed to retrieve data")
