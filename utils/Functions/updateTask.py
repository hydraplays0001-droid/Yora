from utils.shared.shared import tasks


def updateTask():
    print("Press -> ")
    print("1 -> To update the context of a task")
    print("2 -> To update the Done or Not Done of a task (True / False)")

    while True:
        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                for index, key in enumerate(tasks):
                    print(f"{index}. {key} -> {tasks[key]}")

                while True:
                    try:
                        userInput = int(
                            input(
                                "Enter the index number to change its context value: "
                            )
                        )

                        context = input(
                            "Write the context that you want to change to: "
                        )

                        key_list_of_tasks = list(tasks.keys())
                        old_key = key_list_of_tasks[userInput]
                        old_value = tasks[old_key]

                        # change dictionary key
                        del tasks[old_key]
                        tasks[context] = old_value

                        print("Task context updated successfully!")
                        break

                    except IndexError:
                        print("Invalid index number!")
                    except ValueError:
                        print("Enter a number, not a word or symbol!")
                    except KeyboardInterrupt:
                        print("\nExited!")
                        break

            elif choice == "2":
                for index, key in enumerate(tasks):
                    print(f"{index}. {key} -> {tasks[key]}")

                while True:
                    try:
                        userInput = int(
                            input("Enter the index number to change its status: ")
                        )

                        status = input("Enter True or False: ").capitalize()
                        if status not in ("True", "False"):
                            print("Please enter True or False only!")
                            continue

                        key_list_of_tasks = list(tasks.keys())
                        tasks[key_list_of_tasks[userInput]] = status == "True"

                        print("Task status updated successfully!")
                        break

                    except IndexError:
                        print("Invalid index number!")
                    except ValueError:
                        print("Enter a number, not a word or symbol!")
                    except KeyboardInterrupt:
                        print("\nExited!")
                        break

            else:
                print("\nInvalid Choice! Please Enter 1 or 2.")

        except KeyboardInterrupt:
            print("\nExited!")
            break
        except Exception as e:
            print(e)


if __name__ == "__main__":
    updateTask()
