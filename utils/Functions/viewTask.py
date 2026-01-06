from utils.shared.shared import tasks


def viewTasks():
    if not tasks:
        print("Your tasks are empty! ")
    else:
        print("Your tasks Are: ")
        print(tasks)


if __name__ == "__main__":
    viewTasks()
