# Exercise 11
## Write a program that executes a long task:
Timer for 60 seconds.
```python
duration = 60
start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time >= duration:
        break

    print(f"Time passed: {int(elapsed_time)} seconds")
    time.sleep(1)
```
## and has implementation to catch “CRTL+C”:
```python
def signal_handler(sig, frame):
    print("Program stopped.")
    sys.exit(0)
    
signal.signal(signal.SIGINT, signal_handler)
```
## and exit gracefully (without throwing exception).
Output example:
```bash
Time passed: 0 seconds
Time passed: 1 seconds
Time passed: 2 seconds
Time passed: 3 seconds
Program stopped.
```