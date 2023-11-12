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
        print("The password contains unallowed special characters. The allowed characters are:",allowed_special_characters)
        break
else:
    if (long_enough and upper_letters and lower_letters and digit and special_characters):
        print("Good job! Your password matches the criteria!")
    else:
        print("Unfortunately, your password doesn't match the criteria. \nIt should contain: \n- at least 8 characters, \n- both upper and lower letters, \n- digits, \n- special characters.")

# Range loop - prints numbers in a user chosen range that are palindromes (reads the same way forwards as backwards).
print("-----------Palindrome finder-----------")
not_valid = True
while (not_valid):
    start = input("Enter the start of the range: ")
    if (not start.isnumeric()):
        print("You did not enter a number!")
        continue
    end = input("Enter the end of the range: ")
    if (not end.isnumeric()):
        print("You did not enter a number!")
        continue
    start_num = int(start)
    end_num = int(end)
    if (start_num>end_num):
        print("Start number can't be larger than the end number!")
        continue
    if (end_num-start_num>1000000):
        print("Let's not try to break any records today. Please choose a smaller range.")
        continue
    not_valid = False
print("------------------------")
print(f"Palindromes in the range {start_num} to {end_num}:")
count_pal = 0
for num in range(start_num, end_num + 1):
    num_str = str(num)
    if num_str == num_str[::-1]:
        count_pal +=1
        print(num)
if count_pal == 0:
    print("No palindromes were found :(")
