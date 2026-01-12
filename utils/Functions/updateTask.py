from utils.shared.shared import tasks


def updateTask():
    print("Press -> ")
    print("1 -> To update The context a task. ")
    print("2 -> To update The Done or Not Done of a task or (True or False)")
    for value in tasks:
        print(f"{value} -> {tasks[value]}")
    while True:
        try:
            choice = input("Enter your choice: ")
            if choice == "1":
                pass
            elif choice == "2":
                pass
            else:
                print("")
                print("Invalid Choice! Please Enter 1 or 2.")
        except KeyboardInterrupt:
            print()
            print("Exited! ")
            break
        except Exception as e:
            print(e)


if __name__ == "__main__":
    updateTask()
