"""
    function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for    a given subreddit. If an invalid subreddit is given, the function should return 0.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """

    # Construct the URL for the Reddit API request
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set the User-Agent header to identify the source of the requests
    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/YourUsername)'}  # Set your own User-Agent

    try:
        # Make the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx status codes)

        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            print(f"Error: {data['message']}")
            return 0

    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        return 0

    except Exception as ex:
        print(f"Unexpected Error: {ex}")
        return 0
