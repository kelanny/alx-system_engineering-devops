#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-custom-user-agent'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
