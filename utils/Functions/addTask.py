from time import sleep
from utils.shared.shared import tasks


def addTask():
    Task: str = input("Enter Your Task: ")
    sleep(2)
    dictionary: dict[str, bool] = {Task: False}
    tasks.update(dictionary)
    print("Added Task Successfully! ")


if __name__ == "__main__":
    addTask()
