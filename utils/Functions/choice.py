from utils.Functions.deleteTask import delete_task
from utils.Functions.viewTask import viewTasks
from utils.Functions.addTask import addTask


def userChoice():
    try:
        print(f"{'\t' * 8}***-***-TODO LIST APP-***-***{'\t' * 2}")
        print("Press:")
        print("'1' To View The Tasks.")
        print("'2' To Add a Task.")
        print("'3' To Delete a Task.")
        print("'4' To Update The Tasks.")
        print("'5' To Exit.")
        while True:
            choice = input("Enter your choice: ")

            if choice == "1":
                viewTasks()
            elif choice == "2":
                addTask()
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                delete_task()
            elif choice == "4":
                pass
            elif choice == "5" or choice == "exit":
                print("Thanks For Coming Here. ")
                break
            else:
                print("Invalid choice!")
    except KeyboardInterrupt as _:
        print("")
        print("Exiting Program!")
    except ValueError:
        print("Enter A Correct Value! ")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    userChoice()
