import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyRedditBot/1.0 (by /u/YourUsername)'}  # Set your own User-Agent

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            posts = data['data']['children'][:10]

            if not posts:
                print("No posts found.")
            else:
                for post in posts:
                    print(post['data']['title'])

        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
