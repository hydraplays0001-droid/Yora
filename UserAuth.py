import re
import random
import os
import string
from time import sleep
from utils.Functions.choice import userChoice
from UsersName import UsersName

directory = "userDatabase"


def email_exists(directory, email):
    """Search all files in directory for the email"""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    if email in f.read():
                        return True
            except Exception:
                pass
    return False


def auth():
    pattern = r"^[A-Za-z0-9_%#]+(\.[A-Za-z0-9_%#]+)?@[A-Za-z0-9_%#]+\.(edu|com)$"

    print("Want to create an account? Press Y to create the account.")
    print("Press N if you already have an existing account.")

    try:
        while True:
            choice = input("Enter your choice (Y/N): ").lower().strip()

            if choice == "y":
                UsersName()
                print(
                    "\nContinue To With Google 🇬, Apple 🍎, Microsoft 🪟, Facebook 𝐟 , Steam 💨, Twitter 𝕏\n"
                )

                account = input("Enter Your Account That You Want To Continue With: ")

                if re.fullmatch(pattern, account):
                    os.makedirs(directory, exist_ok=True)

                    # Generate random filename
                    length = random.randint(5, 20)
                    random_number = "".join(random.choices(string.digits, k=length))
                    filename = f"{random_number}.txt"
                    filepath = os.path.join(directory, filename)

                    with open(filepath, "w", encoding="utf-8") as file:
                        file.write(account)

                    sleep(1)
                    print("✅ Account Created Successfully!\n")
                    break
                else:
                    print("❌ Invalid Email!")

            elif choice == "n":
                account = input("Enter Your Existing Account: ")

                if re.fullmatch(pattern, account):
                    if email_exists(directory, account):
                        print("\n✅ Welcome!\n")
                        userChoice()
                        break
                    else:
                        print("❌ Email Not Found!")
                else:
                    print("❌ Invalid Email!")

            else:
                print("⚠️ Please enter only Y or N!")

    except KeyboardInterrupt:
        print("\nExited")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    auth()
