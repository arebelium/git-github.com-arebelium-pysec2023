import signal
import time
import sys

def signal_handler(sig, frame):
    print("Program stopped.")
    sys.exit(0)
    
signal.signal(signal.SIGINT, signal_handler)

# Timer for 60 seconds
duration = 60
start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time >= duration:
        break

    print(f"Time passed: {int(elapsed_time)} seconds")
    time.sleep(1)