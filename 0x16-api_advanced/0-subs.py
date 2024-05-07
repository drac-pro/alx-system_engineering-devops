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
        headers = {'User-Agent': 'Python:SubredditSubscriberCounter:v1.2.3 (by /u/drac_prog)'}
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        else:
            print(response.status_code)
            return 0
    except Exception:
        return 0
