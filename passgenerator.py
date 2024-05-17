import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

Use_for = lower_case + upper_case + number + symbols

length_for_pass = input("Enter the password length (hit enter for default : 8): ")

if length_for_pass == "":
    length_for_pass = 8
else:
    length_for_pass = int(length_for_pass)

password = "".join(random.sample(Use_for, length_for_pass))

print("Generated password:", password)
print("Remember to save or write down this password in a secure place.")
