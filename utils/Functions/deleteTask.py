from utils.shared.shared import tasks


def delete_task():
    for index, value in enumerate(tasks):
        print(f"{index} -> {value}, {tasks[value]}")
    keys_list = list(tasks.keys())
    try:
        index_to_remove = int(input("Enter The Index number you want to Delete: "))
        key_to_delete = keys_list[index_to_remove]
        tasks.pop(key_to_delete)
        print(tasks)
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
