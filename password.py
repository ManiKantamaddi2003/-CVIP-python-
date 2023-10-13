import string
import random

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars, special_chars):
    characters = ""
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += special_chars

    if not characters:
        print("Please select at least one character type.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    print("=========================")

    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 4:
                print("Password length should be at least 4 characters.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for password length.")

    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    special_chars = input("Enter special characters to include (if any): ")

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars, special_chars)
    
    if password:
        print(f"Generated Password: {password}")
    else:
        print("Password generation failed. Please check your criteria.")

if __name__ == "__main__":
    main()
