#!/usr/bin/python3
"""
How many subs?
"""

import requests


def number_of_subscribers(subreddit):
    """
    finding number of subscribers
    """
    if subreddit is None:
        return 0
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    agent = {"User-Agent": "ALX project about advanced api"}

    response = requests.get(url, headers=agent).json()

    return response.get("data", {}).get("subscribers", 0)
