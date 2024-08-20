import random
import string

def generate_password(length, use_special_chars=True):
    """Generate a random password of specified length."""
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = lower_chars + upper_chars + digits + special_chars

    if length <= 0:
        return "Password length must be greater than 0."

    if len(all_chars) == 0:
        return "No characters available to generate password."

   
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    password = generate_password(length, use_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
