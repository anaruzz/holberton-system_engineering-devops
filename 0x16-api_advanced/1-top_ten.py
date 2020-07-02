#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
            'user-agent': 'my custom user agent 1.0'
    }
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    try:
        response = response.json()
        children = response.get('data').get('children')
        for item in children:
            print(item['data']['title'])
    except Exception as e:
        print('None')
