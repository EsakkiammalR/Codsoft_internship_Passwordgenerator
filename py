import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    password_length = int(input("Enter the desired password length: "))
    if password_length < 1:
        print("Password length should be at least 1 character.")
    else:
        generated_password = generate_password(password_length)
        print("Generated Password: " + generated_password)
except ValueError:
    print("Please enter a valid password length (a positive integer).")
