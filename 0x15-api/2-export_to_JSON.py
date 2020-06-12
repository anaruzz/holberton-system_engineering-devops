#!/usr/bin/python3
"""
Script that gathers to do data from an api and exports it to a JSON file
"""

if __name__ == '__main__':

    import json
    import requests
    import sys

    if len(sys.argv) < 2:
        print('Usage: {} EMPLOYEE_ID'.format(argv[0]))
        exit()
    user_id = sys.argv[1]
    file_name = '{}.json'.format(user_id)
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get("{}/{}".format(url, user_id), verify=False)
    if response.status_code == 200:
        content = response.json()
        to_do = requests.get(url + '{}/todos'.format(user_id)).json()
        output = {}
        output[user_id] = []
        for row in to_do:
            data = {}
            data["task"] = row.get('title')
            data["completed"] = row.get('completed')
            data["username"] = content.get('username')
            output[user_id].append(data)

        with open(file_name, 'w', encoding='utf-8') as jf:
            json.dump(output, jf)
