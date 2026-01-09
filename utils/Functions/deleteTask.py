# from utils.shared.shared import tasks
tasks = {"Something": False, "asdf": True}


def delete_task():
    for index, value in enumerate(tasks):
        print(f"{index} -> {value}, {tasks[value]}")


if __name__ == "__main__":
    delete_task()
