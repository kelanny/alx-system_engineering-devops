#!/usr/bin/python3
""" Recursively queries the Reddit API, parses the titles of all hot articles,
and prints a sorted count of given keywords.
"""

from collections import Counter
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-custom-user-agent'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            children = data['data']['children']
            if not children and not hot_list:
                return None
            for child in children:
                hot_list.append(child['data']['title'])
            after = data['data']['after']

            if after:
                return count_words(subreddit, word_list, hot_list, after)
            else:
                count = Counter()
                for title in hot_list:
                    words = title.lower().split(' ')
                    for word in word_list:
                        keyword = word.lower()
                        count[keyword] += sum(1 for w in words if w == keyword)

                filtered_count = {k: v for k, v in count.items() if v > 0}

                sorted_count = sorted(filtered_count.items(),
                                      key=lambda item: (-item[1], item[0]))

                for word, cnt in sorted_count:
                    print(f"{word}: {cnt}")
        else:
            return None

    except requests.RequestException:
        return None
