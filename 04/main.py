import random

# While loop - mini password cracker simulator
print("-------------Mini password cracker-------------")
possible_passwords = ["12345", "password", "letmein", "admin", "secure123"]
password = possible_passwords[random.randint(0,len(possible_passwords)-1)]

index = 0
cracked = False
while (index<len(possible_passwords)):
    temp_password = possible_passwords[index]
    if temp_password == password:
        print("The password is:",temp_password)
        print("The password was cracked on the attempt nr.",index+1)
        cracked = True
        break
    index+=1
if not cracked:
    print("This password was impossible to crack!")


# For loop - password strength checker
print("-----------Password strength checker-----------")
input_password = input("Please enter a password:")
print("------------------------")
long_enough = len(input_password)>7
upper_letters = False
lower_letters = False
digit = False
special_characters = False
allowed_special_characters = "!@#$%^&*?"
all_allowed_characters = True

for character in input_password:
    if character.isupper():
        upper_letters=True
    elif character.islower():
        lower_letters=True
    elif character.isnumeric():
        digit=True
    elif character in allowed_special_characters:
        special_characters = True
    else:
        all_allowed_characters = False
        print("The password contains unallowed special characters. The allowed characters are:",special_characters)
        break

if (long_enough and upper_letters and lower_letters and special_characters and all_allowed_characters):
    print("Good job! Your password matches the criteria!")
else:
    print("Unfortunately, your password doesn't match the criteria. \nIt should contain: \n- at least 8 characters, \n- both upper and lower letters, \n- digits, \n- special characters.")

