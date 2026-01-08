# NOTE: Importing two modules :===
# NOTE: From time module importing sleep function for some effects.  :)
# NOTE: From utils.shared.shared importing tasks global variable which a dictionary that stores all the tasks.
from time import sleep
from utils.shared.shared import tasks


# NOTE: Created a Function named 'addTask' For Adding the tasks in a global variable named tasks.
# NOTE: which is a dictionary with a key where is your task and a value that tells that is this task done or not in boolean value.


def addTask():
    Task: str = input("Enter Your Task: ")
    sleep(2)
    tasks.update(dictionary)
    print("Added Task Successfully! ")


if __name__ == "__main__":
    addTask()
