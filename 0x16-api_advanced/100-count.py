#!/usr/bin/python3
""" Script that does headache"""
import requests


def count_words(subreddit, word_list, word_dic={}, after=""):

    if not word_dic:
        for word in word_list:
            word_dic[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in word_dic.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for word in word_list:
            if word[1]:
                print("{}: {}".format(word[0], word[1]))
        return None

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {
        'limit': 100,
        'after': after
    }
    headers = {
            'user-agent': 'my custom user agent 1.0'
    }
    response = requests.get(url, headers=headers, params=params)
    if not response.status_code:
        return None

    try:
        response = response.json()
        data = response.get("data", None)
        after = data.get("after", None)
        children = data.get("children", None)
        for child in children:
            post = child.get("data", None)
            title = post.get("title", None)
            lower = []
            for s in title.split(' '):
                lower.append(s.lower())

            for w in word_list:
                word_dic[w] += lower.count(w.lower())

    except Exception as e:
        return None

    count_words(subreddit, word_list, word_dic, after)
