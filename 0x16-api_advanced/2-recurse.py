#!/usr/bin/python3
"""
importing python modules
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively retrieve and append the titles
    """
    if subreddit is None:
        return None
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    agent = {"User-Agent": "ALX project about advanced api"}

    feedback = requests.get(url, params={"after": after}, headers=agent)

    if feedback.status_code == 200:
        solution = feedback.json().get("data").get("after")
        if not solution:
            return hot_list
        for post in feedback.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        return recurse(subreddit, hot_list, solution)
