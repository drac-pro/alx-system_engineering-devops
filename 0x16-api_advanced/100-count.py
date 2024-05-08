#!/usr/bin/python3
"""defines a function that print count of keywords inall hot
articles in a subreddit"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after='', word_counts=Counter()):
    """print count of keywords in a list of hot articles for given subreddit
    args:
        subreddit: name of the subreddit
        word_list: list of key words
        after: variable for pagination
        word_counts: dict for counting key words
    Returns:
        nothing if fail
    """
    try:
        headers = {'User-Agent':
                   'Python:SubredditKeywordCounter:v1.2.3'}
        url = "https://www.reddit.com/r/{}/hot.json?after={}"\
            .format(subreddit, after)

        sub_res = requests.get(url, headers=headers, allow_redirects=False)
        if sub_res.status_code != 200:
            return None

        if after == '':
            word_list = [w.lower() for w in word_list].sorted()
        data = sub_res.json()['data']

        for article in data['children']:
            title = article['data']['title'].lower()
            word_counts.update(w for w in title.split() if w in word_list)

        if data['after'] is not None:
            return count_words(subreddit, word_list,
                               data['after'], word_counts)
        else:
            for word, count in word_counts.most_common():
                print('{}: {}'.format(word, count))
    except Exception:
        return None
