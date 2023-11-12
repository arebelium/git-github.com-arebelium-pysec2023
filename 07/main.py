class WeakPasswordException(Exception):
    def __init__(self, password, message="Unfortunately, your password doesn't match the criteria. \nIt should contain: \n- at least 8 characters, \n- both upper and lower letters, \n- digits, \n- special characters."):
        self.password = password
        self.message = message
        super().__init__(self.message)

def validate_password(password):
    """Function to validate password strength."""
    long_enough = len(password)>7
    upper_letters = False
    lower_letters = False
    digit = False
    special_characters = False
    allowed_special_characters = "!@#$%^&*?"
    for character in password:
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
        if not(long_enough and upper_letters and lower_letters and digit and special_characters):
            raise WeakPasswordException(password)

## demonstrate use of Exception
print("-------------Built-in exception-------------")
try:
    10/0
except Exception as e:
    print(f"Error: {e}")

## custom Exception
print("-------------Custom exception-------------")
try:
    user_password = input("Enter your password: ")
    validate_password(user_password)
    print("Password is strong. Welcome!")
except WeakPasswordException as e:
    print(f"Error: {e}")

