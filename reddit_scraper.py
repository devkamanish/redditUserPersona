import os
import praw
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

def get_user_data(username, limit=50):
    user = reddit.redditor(username)

    posts = []
    comments = []

    try:
        for post in user.submissions.new(limit=limit):
            posts.append({
                "title": post.title,
                "body": post.selftext,
                "subreddit": post.subreddit.display_name,
                "url": f"https://www.reddit.com{post.permalink}"
            })
    except Exception as e:
        print(f"[ERROR] fetching posts: {e}")

    try:
        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "subreddit": comment.subreddit.display_name,
                "url": f"https://www.reddit.com{comment.permalink}"
            })
    except Exception as e:
        print(f"[ERROR] fetching comments: {e}")

    return {
        "username": username,
        "posts": posts,
        "comments": comments,
    }