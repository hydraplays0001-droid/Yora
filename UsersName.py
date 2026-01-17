import random
import os
import string


def UserInfo():
    length = random.randint(1, 20)

    # Generate a random number string of that length
    random_number = "".join(random.choices(string.digits, k=length))

    filename = f"{random_number}.txt"

    os.open(filename, os.O_CREAT | os.O_WRONLY)

    first_name = input("Enter Your First Name: ")
    last_name = input("Enter Your Last Name (Optional): ")
    if last_name is None:
        last_name = ""

    with open(f"UsersName/{filename}", "w") as file:
        file.write(f"{first_name} {last_name}")


if __name__ == "__main__":
    UserInfo()
