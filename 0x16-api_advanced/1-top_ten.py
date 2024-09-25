#!/usr/bin/python3
"""import modules"""

import requests


def top_ten(subreddit):
    """
    Retrieve and print the titles of the top ten hot posts for a
    given subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit for which to
        retrieve the top ten hot posts.
    """
    if subreddit is None:
        return 0
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    agent = {"User-Agent": "ALX project about advanced api"}

    feedback = requests.get(url, params={"limit": 10}, headers=agent)

    if feedback.status_code == 200:
        for post in feedback.json().get('data', {}).get('children', []):
            print(post.get('data').get('title'))
    else:
        print(None)
