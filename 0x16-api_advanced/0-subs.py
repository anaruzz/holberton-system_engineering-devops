#!/usr/bin/python3
"""
Script that gathers to do data from an api
"""


import requests
import sys


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
            'user-agent': 'my custom user agent 1.0'
    }
    response = requests.get(url, headers=headers)
    response = response.json()
    return response['data']['subscribers']
