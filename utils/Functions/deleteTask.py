from utils.shared.shared import tasks
from time import sleep


def delete_task():
    if not tasks:
        print("Your Tasks Are Empty")
    else:
        for index, value in enumerate(tasks):
            print(f"{index} -> {value}, {tasks[value]}")
        keys_list = list(tasks.keys())
        try:
            index_to_remove = int(input("Enter The Index number you want to Delete: "))
            key_to_delete = keys_list[index_to_remove]
            tasks.pop(key_to_delete)
            sleep(2)
            print("Task deleted Successfully! ")

        except IndentationError:
            print("Too smaller or bigger number! ")
        except ValueError:
            print("Enter A Number")
        except KeyboardInterrupt:
            print("Exited")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    delete_task()
