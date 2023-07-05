import itertools
import string

def generate_passwords():
    password_length = range(8, 13)  # Password length between 8 and 12 characters

    lowercase_letters = string.ascii_lowercase  # Lowercase letters
    uppercase_letters = string.ascii_uppercase  # Uppercase letters
    digits = string.digits  # Numbers
    special_characters = string.punctuation  # Special characters

    # Combine all available characters
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate all possible combinations of characters with the specified length
    passwords = []
    for length in password_length:
        passwords.extend(''.join(p) for p in itertools.product(all_characters, repeat=length))

    return passwords

def save_passwords_to_file(passwords, filename):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

passwords = generate_passwords()
save_passwords_to_file(passwords, 'passwords.txt')
