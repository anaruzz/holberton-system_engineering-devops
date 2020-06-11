#!/usr/bin/python3
"""
Script that gathers all to do data from an api and exports it to a JSON file
"""

if __name__ == '__main__':

    import json
    import requests
    import sys

    file_name = 'todo_all_employees.json'
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        content = response.json()
        all_data = {}
        for user in content:
            user_id = user.get('id', 1)
            all_data[user_id] = []
            to_do = requests.get(url + '{}/todos'.format(user_id)).json()
            for row in to_do:
                user_data = {}
                user_data["task"] = row.get('title')
                user_data["completed"] = row.get('completed')
                user_data["username"] = user.get('username')
                all_data[user_id].append(user_data)
        with open(file_name, 'w', encoding='utf-8') as jf:
            json.dump(all_data, jf)
