import requests

def fetch_post(post_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    )
    return response.json()