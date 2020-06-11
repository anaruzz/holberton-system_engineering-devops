#!/usr/bin/python3
"""
Script that gathers to do data from an api and exports it to a csv file
"""

if __name__ == '__main__':
    import csv
    import requests
    import sys

    if len(sys.argv) < 2:
        print('Usage: {} EMPLOYEE_ID'.format(argv[0]))
        exit()

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
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for row in to_do:
                writer.writerow([
                    int(user_id),
                    content.get('username', ''),
                    row.get('completed', False),
                    row.get('title', '')
                ])
