from random import choice
from string import ascii_letters, digits, punctuation

def generate_password(password_length = 20):

    # string containing all possible characters
    all_possible_characters = ascii_letters + digits + punctuation

    # choose a random character and concatenate it into a list of length == password length
    return ''.join(choice(all_possible_characters) for character in range(password_length))


print(generate_password(25))