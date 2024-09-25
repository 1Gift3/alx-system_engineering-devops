#!/usr/bin/python3
"""
get modules
"""
import requests


def number_of_subscribers(subreddit):
    """
    finding of subscribers in
    a reddit channel
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyCustomUserAgentNetwork/1.0'}
    try:
        feedback = requests.get(url, headers=headers, allow_redirects=False)

        if feedback.status_code == 200:
            content = feedback.json()
            return content['data']['subscribers']
        else:
            return 0
    except Exception as err:
        print(f'Error: {e}')
        return 0
