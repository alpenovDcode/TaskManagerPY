from task_manager.modules.task import (add_new_task,
                                       update_existing_task,
                                       delete_existing_task,
                                       get_tasks)

def main():
    while True:
        print("\nУправление задачами")
        print("1. Добавить задачу")
        print("2. Обновить задачу")
        print("3. Удалить задачу")
        print("4. Показать все задачи")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            description = input("Введите описание задачи: ")
            add_new_task(description)
            print("Задача добавлена.")
        elif choice == "2":
            task_id = int(input("Введите ID задачи: "))
            description = input("Введите новое описание задачи (оставьте пустым, чтобы не изменять): ")
            status = input("Введите новый статус задачи (оставьте пустым, чтобы не изменять): ")
            updated_task = update_existing_task(task_id, description or None, status or None)
            if updated_task:
                print("Задача обновлена.")
            else:
                print("Задача не найдена.")
        elif choice == "3":
            task_id = int(input("Введите ID задачи, которую хотите удалить: "))
            delete_existing_task(task_id)
            print("Задача удалена.")
        elif choice == "4":
            tasks = get_tasks()
            if tasks:
                for t in tasks:
                    print(f'ID: {t["id"]}, Описание: {t["desription"]}, Статус: {t["status"]}')
            else:
                print("Задач нет.")
        elif choice == "5":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите от 1 до 5.")

if __name__ == "__main__":
    main()