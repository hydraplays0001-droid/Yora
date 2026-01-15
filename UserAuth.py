print("Want To create an account? Press Y to Create The account. ")
print("Press Y For Existing account That You have. ")
choice = input("Enter Your Choice -- (Y)/(N): ").lower().strip()
while True:
    if choice == "Y":
        account = input("Enter Your Existing Account: ")
    elif choice == "N":
        break
    else:
        print("Please enter only Y or N! ")
