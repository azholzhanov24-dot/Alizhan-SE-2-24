import os

tasks = []
next_id = 1


def load_tasks():
    global next_id, tasks
    if not os.path.exists("tasks.txt"):
        return

    file = open("tasks.txt", "r")
    for line in file:
        line = line.strip()
        if line == "":
            continue

        parts = line.split("|")
        task_id = int(parts[0])
        title = parts[1]

        if parts[2] == "1":
            done = True
        else:
            done = False

        task = {"id": task_id, "title": title, "done": done}
        tasks.append(task)

        if task_id >= next_id:
            next_id = task_id + 1

    file.close()


def save_tasks():
    file = open("tasks.txt", "w")
    for task in tasks:
        if task["done"] == True:
            status_val = "1"
        else:
            status_val = "0"

        line = str(task["id"]) + "|" + task["title"] + "|" + status_val + "\n"
        file.write(line)
    file.close()


def add_task():
    global next_id
    title = input("Enter task title: ")
    task = {"id": next_id, "title": title, "done": False}
    tasks.append(task)
    next_id = next_id + 1
    print("Task added successfully.")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
        return

    for task in tasks:
        if task["done"] == True:
            status = "Done"
        else:
            status = "Not Done"
        print("[" + str(task["id"]) + "] " + task["title"] + " | " + status)


def mark_done():
    task_id = int(input("Enter task ID: "))
    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print("Task marked as Done.")
            found = True
            break
    if found == False:
        print("Task not found.")


def delete_task():
    task_id = int(input("Enter task ID: "))
    found = False
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("Task deleted.")
            found = True
            break
    if found == False:
        print("Task not found.")


def show_stats():
    total = len(tasks)
    if total == 0:
        print("Total tasks: 0")
        print("Done: 0")
        print("Not done: 0")
        print("Completion: 0%")
        return

    done_count = 0
    for task in tasks:
        if task["done"] == True:
            done_count = done_count + 1

    not_done = total - done_count
    percentage = int((done_count / total) * 100)

    print("Total tasks: " + str(total))
    print("Done: " + str(done_count))
    print("Not done: " + str(not_done))
    print("Completion: " + str(percentage) + "%")


load_tasks()

while True:
    print("\n=== STUDENT TASK MANAGER ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Show Statistics")
    print("6. Save & Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        show_stats()
    elif choice == "6":
        save_tasks()
        break
    else:
        print("Invalid option. Try again.")