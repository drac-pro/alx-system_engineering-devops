#!/usr/bin/python3
"""defines a function for getting number of subscribers in a subreddit"""
import requests


def top_ten(subreddit):
    """returns the number of subscribers for given subreddit
    args:
        subreddit: name of the subreddit
    Returns:
        number of subscribers
    """
    try:
        headers = {'User-Agent':
                   'Python:SubredditHotPosts:v1.2.3'}
        url = "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit)
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        [print(c['data']['title']) for c in
         response.json()['data']['children']]
    except Exception:
        print(None)
