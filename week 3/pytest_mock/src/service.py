from database import get_user
from api import fetch_post


def user_name(user_id):
    user = get_user(user_id)
    return user["name"]


def post_title(post_id):
    post = fetch_post(post_id)
    return post["title"]