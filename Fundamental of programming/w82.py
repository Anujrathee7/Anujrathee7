import string
import random

letter = string.ascii_letters
digits = string.digits
special = string.punctuation

comb = letter+digits+special

random.seed(8292)

length = input("Enter the length of the password:\n")
while True:
    if(int(length) > 0):
        break
    else:
        print("Password length must be a positive integer.")
        length = input("Enter the length of the password:\n")

password = ''.join(random.choice(comb) for _ in range(int(length)))

print("Generated password:",password)

