#!/usr/bin/python3
"""
queries the Reddit API and returns
the number of subscribers
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    queries the Reddit API and returns the number of subscribers

    Args:
        subreddit (str): name of subreffit

    Returns:
        int: number of subscribers
    """

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': '0x16-api_advanced:project:\
            v1.0.0 (by /u/firdaus_cartoon_jr)'}
    params = {
            "after": after,
            "count": count,
            "limit": 10
            }

    response = requests.get(url, headers=headers, params=params,
            allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get(("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list

