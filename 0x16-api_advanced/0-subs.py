
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
    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    agent = {"User-Agent": "ALX project about advanced api"}

    response = requests.get(url, headers=agent).json()

    return response.get("data", {}).get("subscribers", 0)
