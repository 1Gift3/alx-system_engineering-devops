#!/usr/bin/python3
"""
imported request module
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    counter function of words
    """
    feedback = requests.get(f"https://www.reddit.com/r/{subreddit}/hot.json",
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if feedback.status_code != 200:
        return None

    reponse_json = feedback.json()
    appearance = []
    for d in reponse_json.get("data").get('children'):
        appearance.append(d.get('data').get('title'))
    if not appearance:
        return None
    word_list = list(dict.fromkeys(word_list))
    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for data in appearance:
        data_split = data.split(' ')
        for word in word_list:
            for sm in data_split:
                if sm.lower() == word.lower():
                    word_count[word] += 1

    if reponse_json.get("data").get("after") is None:
        sorts = sorted(word_count.items(), key=lambda kv: kv[0])
        sorts = sorted(word_count.items(), key=lambda kv: kv[1], reverse=True)
        for key, value in sorts:
            if value != 0:
                print(f'{key}: {value}')
    else:
        return count_words(subreddit, word_list, word_count,
                           reponse_json.get("data").get("after"))
