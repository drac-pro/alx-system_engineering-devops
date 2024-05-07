#!/usr/bin/python3
"""defines a function for getting all hot articles in a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """returns a list of hot articles for given subreddit    args:
        subreddit: name of the subreddit
        hot_list: list to pupolate
        after: variable for pagination
    Returns:
        list of hot articles
    """
    try:
        headers = {'User-Agent':
                   'Python:SubredditHotArticles:v1.2.3'}
        url = "https://www.reddit.com/r/{}/hot.json?after={}"\
            .format(subreddit, after)

        sub_res = requests.get(url, headers=headers, allow_redirects=False)
        if sub_res.status_code != 200:
            return None

        data = sub_res.json()['data']
        [hot_list.append(c['data']['title']) for c in
         data['children']]
        if data['after'] is not None:
            return recurse(subreddit, hot_list, data['after'])
        else:
            return hot_list
    except Exception:
        return None
