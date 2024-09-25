#!/usr/bin/python3
"""
imported modules
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given
    """
    if subreddit is None:
        return 0
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "ALX project about advanced api"}

    response = requests.get(url, headers=user_agent).json()

    return response.get("data", {}).get("subscribers", 0)
