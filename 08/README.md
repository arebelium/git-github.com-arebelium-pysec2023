# Exercise 8
As the code was written on a Windows machine - a synthetic messages file was created and saved in the exercise directory under data/messages.
## Read /var/log/messages
```python
with open(filepath, 'r') as file:
    for line in file:
        ...
```
## Find all the logs which pertain to USB and print them out selectively
```python
if 'usb' in line.lower():
    print(line.strip())
```