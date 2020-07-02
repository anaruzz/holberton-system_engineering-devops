#!/usr/bin/python3
"""
Script that queries the Reddit API and
returns the number of subscribers
"""


import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            'user-agent': 'my custom user agent 1.0'
    }
    response = requests.get(url, headers=headers)
    response = response.json()
    try:
        return response['data']['subscribers']
    except Exception as e:
        return 0
