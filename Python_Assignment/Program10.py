import random
import string

def generate_strong_password(length):
    
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    shuffled_characters = random.sample(all_characters, len(all_characters))

    password = ''.join(random.sample(shuffled_characters, length))

    return password

# Example usage
length = 12 
password = generate_strong_password(length)
print("Generated Password:", password)
