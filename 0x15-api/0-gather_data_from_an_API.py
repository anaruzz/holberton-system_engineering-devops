#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import requests

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get("{}/{}".format(url, user_id), verify=False)
    if response.status_code == 200:
        content = response.json()
        employee_name = content.get('name')
        total_tasks = 0
        done_tasks = []
        done_tasks_number = 0
        to_do = requests.get(url + '{}/todos'.format(user_id)).json()
        total_tasks = len(to_do)
        # print('employee_name: {}'.format(employee_name))
        # print('total_tasks: {}'.format(total_tasks))
        for task in to_do:
            if task.get('completed', None):
                done_tasks.append(task.get('title'))
        done_tasks_number = len(done_tasks)
        # print('done tasks number {}'.format(done_tasks_number))
        print('Employee {} is done with tasks({}/{}):'.format(
                employee_name, done_tasks_number, total_tasks))
        for task in done_tasks:
            print('\t {}'.format(task))