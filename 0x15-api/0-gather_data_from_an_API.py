#!/usr/bin/python3
"""
Script that gathers to do data from an api
"""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) < 2:
        print('Usage: {} EMPLOYEE_ID'.format(argv[0]))
        exit()

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/'
    req = requests.get("{}/{}".format(url, user_id), verify=False)
    if req.status_code == 200:
        content = req.json()
        employee_name = content.get('name')
        total_tasks = 0
        done_tasks = []
        done_tasks_number = 0
        to_do = requests.get(url + '{}/todos'.format(user_id)).json()
        total_tasks = len(to_do)
        for task in to_do:
            if task.get('completed', None):
                done_tasks.append(task.get('title'))
        done_tasks_number = len(done_tasks)
        print('Employee {} is done with tasks({}/{}):'.format(
                employee_name, done_tasks_number, total_tasks))
        for task in done_tasks:
            print('\t {}'.format(task))
