import random
import string

def generate_password(length):
    # All possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

# Run the program
main()
