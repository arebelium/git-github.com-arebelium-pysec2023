import os
import time

def print_file_stats(file_path):
    stats = os.stat(file_path)

    print(f"File: {file_path}")
    print(f"Size: {stats.st_size} bytes")
    print(f"Creation Time: {time.ctime(stats.st_ctime)}")
    print(f"Last Access Time: {time.ctime(stats.st_atime)}")
    print(f"Last Modification Time: {time.ctime(stats.st_mtime)}")

def print_directory_contents(path, indent = "----"):
    for entry in os.listdir(path):
        print(f"{indent}{entry}")
        entry_full_path = os.path.join(path,entry)
        if os.path.isdir(entry_full_path):
            print_directory_contents(entry_full_path, indent+"----") 


starting_directory = input("Enter starting directory:")
base_path = os.path.basename(starting_directory)
print(base_path)
if os.path.isdir(starting_directory):
    print_directory_contents(starting_directory)

file_path = input("Enter path to the file for which to display stats:")
if os.path.isfile(file_path):
    print_file_stats(file_path)
else:
    print("Are you sure you entered a path to a specific file?")