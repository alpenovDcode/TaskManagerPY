tasks = []

def add_task(desription, status="в процессе"):
    task_id = len(tasks) + 1
    # ключ id, desription, status
    # значение id, desription, status
    task = {'id':task_id, 'desription':desription, 'status':status}
    tasks.append(task)
    return task


'''
['id':1, 'desription':asd, 'status':status,]
['id':2, 'desription':asd, 'status':status,]
['id':3, 'desription':asd, 'status':status]
'''

def update_task(task_id, desription=None, status=None):
    for task in tasks:
        if task['id'] == task_id:
            if desription:
                task['desription'] = desription
            if status:
                task['status'] = status
            return task
        return None

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id] # True, False

def get_tasks():
    return tasks
