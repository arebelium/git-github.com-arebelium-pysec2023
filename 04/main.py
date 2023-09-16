import random

# While loop - mini password cracker simulator
print("----Mini password cracker----")
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
print("----Mini strength checker----")
