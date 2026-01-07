from utils.Functions.viewTask import viewTasks


def userChoice():
    while True:
        print(f"{'\t' * 8}***-***-TODO LIST APP-***-***{'\t' * 2}")
        print("Press:")
        print("'1' To View The Tasks.")
        print("'2' To Add a Task.")
        print("'3' To Delete a Task.")
        print("'4' To Update The Tasks.")
        print("'5' To Exit.")

        choice = input("Enter your choice: ")

        if choice == "1":
            viewTasks()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            print("Thanks For Coming Here. ")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    userChoice()
