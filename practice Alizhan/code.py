tasks = []
next_id = 1

def add_task():
    global next_id
    title = input("Enter task title: ")
    tasks.append({"id": next_id, "title": title, "done": False})
    next_id += 1
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks.")
        return

    for t in tasks:
        status = "Done" if t["done"] else "Not Done"
        print(f'[{t["id"]}] {t["title"]} | {status}')

def mark_done():
    view_tasks()
    task_id = int(input("Enter task ID: "))

    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            print("Task marked as Done.")
            return

    print("Task not found.")

def delete_task():
    task_id = int(input("Enter task ID: "))

    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            print("Task deleted.")
            return

    print("Task not found.")

def show_stats():
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    not_done = total - done
    percent = (done / total * 100) if total else 0

    print(f"Total: {total}")
    print(f"Done: {done}")
    print(f"Not done: {not_done}")
    print(f"Completion: {percent:.0f}%")

def save_tasks():
    with open("tasks.txt", "w") as f:
        for t in tasks:
            f.write(f'{t["id"]}|{t["title"]}|{1 if t["done"] else 0}\n')

def load_tasks():
    global next_id
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tid, title, done = line.strip().split("|")
                tasks.append({
                    "id": int(tid),
                    "title": title,
                    "done": done == "1"
                })
        if tasks:
            next_id = max(t["id"] for t in tasks) + 1
    except FileNotFoundError:
        pass

while True:
    print("\n=== STUDENT TASK MANAGER ===")
    menu = input(
        "1. Add Task\n"
        "2. View Tasks\n"
        "3. Mark Task as Done\n"
        "4. Delete Task\n"
        "5. Show Statistics\n"
        "6. Save & Exit\n"
        "Choose option: "
    )

    if menu == "1":
        add_task()
    elif menu == "2":
        view_tasks()
    elif menu == "3":
        mark_done()
    elif menu == "4":
        delete_task()
    elif menu == "5":
        show_stats()
    elif menu == "6":
        save_tasks()
        print("Exiting...")
        break
    else:
        print("Invalid option")