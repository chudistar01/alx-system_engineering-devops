#!/usr/bin/python3
"""
queries the Reddit API and returns
the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers

    Args:
        subreddit (str): name of subreffit

    Returns:
        int: number of subscribers
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': '0x16-api_advanced:\
            project:v1.0.0 (by /u/firdaus_cartoon_jr)'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.RequestException:
        return 0
