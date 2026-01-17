import re
from time import sleep
from utils.Functions.choice import userChoice
from UserInfo import UserInfo


def auth():
    pattern = r"^[A-Za-z0-9_%#]+(\.[A-Za-z0-9_%#]+)?+@[A-Za-z0-9_%#]+\.(edu|com)$"
    print("Want to create an account? Press Y to create the account.")
    print("Press N if you already have an existing account.")

    try:
        while True:
            choice = input("Enter your choice (Y/N): ").lower().strip()

            if choice == "y":
                UserInfo()
                print(
                    "\nContinue To With Google 🇬, Apple 🍎, Microsoft 🪟, Facebook 𝐟 , Steam 💨, Twitter 𝕏\n"
                )
                account = input("Enter Your Account That You Want To Continue With: ")
                if re.fullmatch(pattern, account):
                    with open("userDatabase/accounts.txt", "a") as file:
                        file.write(f"{account}")
                        sleep(2)
                        print("Account Created Successfully! ")
                else:
                    print("Invalid Email! ")
            elif choice == "n":
                account = input("Enter Your Existing Account: ")
                if re.fullmatch(pattern, account):
                    if account in open("userDatabase/accounts.txt"):
                        print("\nWelcome! \n")
                        userChoice()
                    else:
                        print("Email Not Found! ")
                else:
                    print("Invalid! ")
            else:
                print("Please enter only Y or N!")
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("\nExited")


if __name__ == "__main__":
    auth()
