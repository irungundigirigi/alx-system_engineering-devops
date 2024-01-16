import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to retrieve the titles of all hot articles for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.
    - hot_list (list): A list to store the titles of hot articles.
    - after (str): The 'after' parameter for pagination in the Reddit API.

    Returns:
    - list or None: A list containing the titles of all hot articles, or None if the subreddit is invalid or has no posts.
    """
    if after is None:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/YourUsername)'}  # Set your own User-Agent

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            posts = data['data']['children']
            after = data['data']['after']

            if not posts:
                return hot_list

            for post in posts:
                hot_list.append(post['data']['title'])

            return recurse(subreddit, hot_list, after)

        else:
            print(f"Error: {data['message']}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
