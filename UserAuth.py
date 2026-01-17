import re

print("Want to create an account? Press Y to create the account.")
print("Press N if you already have an existing account.")

try:
    while True:
        choice = input("Enter your choice (Y/N): ").lower().strip()

        if choice == "y":
            print(
                "Continue To With Google 🇬, Apple 🍎, Microsoft 🪟, Facebook 𝐟 , Steam 💨, Twitter 𝕏"
            )
            break
        elif choice == "n":
            account = input("Enter Your Existing Account: ")
            pattern = (
                r"^[A-Za-z0-9_%#]+(\.[A-Za-z0-9_%#]+)?+@[A-Za-z0-9_%#]+\.(edu|com)$"
            )
            if re.fullmatch(pattern, account):
                print("Valid")
            else:
                print("Invalid! ")
        else:
            print("Please enter only Y or N!")
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("\nExited")
