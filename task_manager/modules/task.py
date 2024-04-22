import task_manager.data.storage

storage_id = ""

def add_new_task(description):
    return task_manager.data.storage.add_task(description)


def update_existing_task(task_id, description=None, status=None):
    return task_manager.data.storage.update_task(task_id, description, status)


def delete_existing_task(task_id):
    task_manager.data.storage.delete_task(task_id)


def get_tasks():
    return task_manager.data.storage.get_tasks()