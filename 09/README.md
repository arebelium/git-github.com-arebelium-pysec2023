# Exercise 9
User has to enter first path to a directory - program will print the files in a hierarchical way.<br>
After that user has to enter path to a specific file to get stats for it.
## Create a program which can recursively traverse directories and print the file listing in a hierarchical way
```python
def print_directory_contents(path, indent = "----"):
    for entry in os.listdir(path):
        print(f"{indent}{entry}")
        entry_full_path = os.path.join(path,entry)
        if os.path.isdir(entry_full_path):
            print_directory_contents(entry_full_path, indent+"----") 
```
## For any given filename list out all the stats related to the file such as size, creation time, etc..
```python
def print_file_stats(file_path):
    stats = os.stat(file_path)

    print(f"File: {file_path}")
    print(f"Size: {stats.st_size} bytes")
    print(f"Creation Time: {time.ctime(stats.st_ctime)}")
    print(f"Last Access Time: {time.ctime(stats.st_atime)}")
    print(f"Last Modification Time: {time.ctime(stats.st_mtime)}")
```
