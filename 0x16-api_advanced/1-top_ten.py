#!/usr/bin/python3
"""
Function that queries the Reddit API and prints titles of the first 10 hot
posts listed for a given subreddit
"""
import requests

def top_ten(subreddit):
    """
    Query Reddit API - if not a valid subreddit, print None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    res = requests.get(url, headers={"User-Agent": "Custom"},params={"limit": 10})

    if res.status_code == 200:
        for i in res.json().get("data").get("children"):
            d = i.get("data")
            title = d.get("title")
            print(title)
    else:
        print(None)
