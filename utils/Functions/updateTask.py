from utils.shared.shared import tasks


def updateTask():
    for value in tasks:
        print(f"{value} -> {tasks[value]}")


if __name__ == "__main__":
    updateTask()
