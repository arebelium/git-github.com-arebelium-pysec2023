filepath = 'data/messages'

# prints all logs from the file that coontain the string 'usb'.
try:
    with open(filepath, 'r') as file:
        for line in file:
            if 'usb' in line.lower():
                print(line.strip())
except Exception as e:
    print(f"Error: {e}")

