import random

password = ""
for i in range(8):
    i = chr(random.randint(33, 126))
    password = i + password
print(password)


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890"
pass_len = int(input("How long would you like your password to be? "))
new_pass = ""

for i in range(0, pass_len):
    password_char = random.choice(chars)
    new_pass = new_pass + password_char
print(new_pass.capitalize())
