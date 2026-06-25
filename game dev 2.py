import random
import string
print("------ WELCOME TO PASSWORD GENERATOR ------")
length = int(input("Enter the desired password length (8-20): "))
while length < 8 or length > 20:
    print("Invalid input. Please enter a number between 8 and 20.")
    length = int(input("Enter the desired password length (8-20): "))
include_uppercase = input("Include uppercase letters? (y/n): ").lower()
while include_uppercase not in ('y', 'n'):
    print("Invalid input. Please enter 'y' or 'n'.")
    include_uppercase = input("Include uppercase letters? (y/n): ").lower()
include_numbers = input("Include numbers? (y/n): ").lower()
while include_numbers not in ('y', 'n'):
    print("Invalid input. Please enter 'y' or 'n'.")
    include_numbers = input("Include numbers? (y/n): ").lower()
include_symbols = input("Include symbols? (y/n): ").lower()
while include_symbols not in ('y', 'n'):        
    print("Invalid input. Please enter 'y' or 'n'.")
    include_symbols = input("Include symbols? (y/n): ").lower()
characters = string.ascii_lowercase
if include_uppercase == 'y':
    characters += string.ascii_uppercase
if include_numbers == 'y':  
    characters += string.digits 
if include_symbols == 'y':
    characters += string.punctuation
password = ''
for i in range(length):
    password += random.choice(characters)
print("Generated password:", password)
