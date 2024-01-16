#!/usr/bin/python3
""" Function to query subscribers on a given Reddit Subreddit."""

import requests

def number_of_subscribers(subreddit):
    """ Returns the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanvced:v1.0.0 (by /u/AgitatedPersimmon212)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
