import threading

cracked = False
num_threads = 5
threads = []

def password_cracker(start, end, thread_number):
    global cracked
    for index in range(start, end):
        temp_password = possible_passwords[index]
        if temp_password == password:
            print(f"The password is: {temp_password}")
            print(f"The password was cracked on the attempt nr. {index - start} in {thread_number}. thread")
            cracked = True
            break

# get possible passwords
try:
    with open('data/top1000000_passwords.txt', 'r') as file:
        possible_passwords = [line.strip() for line in file]
except Exception as e:
    possible_passwords = ["12345", "password", "letmein", "admin", "secure123"]

# user enters their password
password = input("Enter password:")

# calculate the password range for each thread
password_range = len(possible_passwords) // num_threads

# create threads
for i in range(num_threads):
    start = i * password_range
    if i != num_threads - 1:
        end = (i + 1) * password_range 
    else:
        end = len(possible_passwords)
    thread = threading.Thread(target=password_cracker, args=(start, end, i + 1))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

if not cracked:
    print("This password was impossible to crack!")
