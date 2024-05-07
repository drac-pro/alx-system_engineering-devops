#!/usr/bin/python3
"""defines a function for getting number of subscribers in a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for given subreddit
    args:
        subreddit: name of the subreddit
    Returns:
        number of subscribers
    """
    try:
        headers = {'User-Agent': 'Python:SubredditSubscriberCount:v1.2.3'}
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        else:
            return 0
    except Exception:
        return 0
