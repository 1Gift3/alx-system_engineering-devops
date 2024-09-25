#!/usr/bin/python3
""" Module for counting word occurrences in subreddit hot posts """

import re
import requests


def count_word_occurrences(red, search_terms, count_dict={}, next_token=""):
    """
    Count how many times specified words appear in hot posts of a subreddit.

    Args:
        red (str): The name of the subreddit to analyze.
        search_terms (list): A list of words to count.
        count_dict (dict, optional): A dictionary to store counts.
                                      Defaults to {}.
        next_token (str, optional): A Reddit post identifier for pagination.
                                    Defaults to ""
    """
    if red is None:
        return None

    endpoint = "http://www.reddit.com/r/{}/hot.json?limit=100".format(
        red
        )
    headers = {"User-Agent": "ALX project about advanced API"}

    response = requests.get(
        endpoint, params={"after": next_token}, headers=headers
        )

    if response.status_code == 200:
        next_token = response.json().get("data").get("after")
        if not next_token:
            sorted_counts = sorted(
                count_dict.items(), key=lambda x: (-x[1], x[0])
                )
            for term, count in sorted_counts:
                print('{}: {}'.format(term, count))
            return
        for post in response.json().get("data").get("children"):
            title = post.get("data").get("title").lower()
            for term in search_terms:
                term = term.lower()
                if term in title:
                    count_dict[term] = count_dict.get(term, 0) + 1
        return count_word_occurrences(
            red, search_terms, count_dict, next_token
            )
