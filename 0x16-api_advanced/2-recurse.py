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

    # Set the User-Agent header to identify the source of the requests
    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/YourUsername)'}  # Set your own User-Agent

    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx status codes)

        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            posts = data['data']['children']
            after = data['data']['after']

            # Check if there are no more posts
            if not posts:
                return hot_list

            # Extract titles and append them to the hot_list
            for post in posts:
                hot_list.append(post['data']['title'])

            # Recursively call the function with the 'after' parameter for the next page
            return recurse(subreddit, hot_list, after)

        else:
            print(f"Error: {data['message']}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return None

    except Exception as ex:
        print(f"Unexpected Error: {ex}")
        return None
