#!/usr/bin/python3
"""
Script that gathers to do data from an api
"""

if __name__ == '__main__':
    import csv
    import requests
    import sys

    user_id = sys.argv[1]
    file_name = '{}.csv'.format(user_id)
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get("{}/{}".format(url, user_id), verify=False)
    if response.status_code == 200:
        content = response.json()
        employee_name = content.get('name')
        to_do = requests.get(url + '{}/todos'.format(user_id)).json()
        with open(file_name, 'w', encoding='utf-8') as csvfile:
            fieldnames = ['employee_id', 'name', 'task_status', 'title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)
            for row in to_do:
                writer.writerow({'employee_id': user_id, 'name': employee_name,
                                'task_status': row.get('completed'),
                                'title': row.get('title')})
