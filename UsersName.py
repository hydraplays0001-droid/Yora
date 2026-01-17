import random
import os
import string


def UsersName():
    # Ensure directory exists
    directory = "UsersName"
    os.makedirs(directory, exist_ok=True)

    # Generate random number length (1–20 digits)
    length = random.randint(1, 20)
    random_number = "".join(random.choices(string.digits, k=length))

    filename = f"{random_number}.txt"
    filepath = os.path.join(directory, filename)

    first_name = input("Enter Your First Name: ").strip()
    last_name = input("Enter Your Last Name (Optional): ").strip()

    # Write to file
    with open(filepath, "w") as file:
        if last_name:
            file.write(f"{first_name} {last_name}")
        else:
            file.write(first_name)

    print(f"File created at: {filepath}")


if __name__ == "__main__":
    UsersName()
