#!/usr/bin/python3
"""
queries the Reddit API and returns
the number of subscribers
"""

import requests


def top_ten(subreddit):
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
            "limit": 10
            }

    response = requests.get(url, headers=headers, params=params,
            allow_redirects=False)


    if response.status_code == 404:
        print("None")
        return

    results = response.json().get(("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
