from utils.shared.shared import tasks
from time import sleep


def viewTasks():
    if not tasks:
        print("Your tasks are empty! ")
    else:
        sleep(1.4)
        print("Your tasks Are: ")
        print(tasks)


if __name__ == "__main__":
    viewTasks()
