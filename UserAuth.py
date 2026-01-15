print("Want to create an account? Press Y to create the account.")
print("Press N if you already have an existing account.")

try:
    while True:
        choice = input("Enter your choice (Y/N): ").lower().strip()

        if choice == "y":
            break
        elif choice == "n":
            account = input("Enter your existing account: ")
            break
        else:
            print("Please enter only Y or N!")
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("\nExited")
