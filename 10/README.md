# Exercise 10
## Explore Python Threading module
```python
for i in range(num_threads):
    ...
    thread = threading.Thread(target=password_cracker, args=(start, end, i + 1))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```
## Create a meaningful example demonstrating use of the mentioned module
Improved the code from exercise 4 to crack the password in threads.
