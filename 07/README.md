# Exercise 7
## Demonstrate use of Exception
Error when dividing by zero.
```python
try:
    10/0
except Exception as e:
    print(f"Error: {e}")
```
## Can you write your own defined exception?
Exception when user enters a weak password (used code from Exercise 4).
```python
class WeakPasswordException(Exception):
    def __init__(self, password, message="Unfortunately, your password doesn't match the criteria. \nIt should contain: \n- at least 8 characters, \n- both upper and lower letters, \n- digits, \n- special characters."):
        self.password = password
        self.message = message
        super().__init__(self.message)
```