import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/YourUsername)'}  # Set your own User-Agent

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            print(f"Error: {data['message']}")
            return 0

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
