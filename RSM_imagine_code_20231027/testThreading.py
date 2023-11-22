import threading
import time

# Function to print lines from 1 to n
def printLine(n):
    for i in range(1, n + 1):
        print(f"Line {i}")
        time.sleep(1)  # Sleep for 1 second between lines

# Create a thread for printLine(9)
print_line_thread = threading.Thread(target=printLine, args=(9,))

# Start the print_line_thread
print_line_thread.start()

# Keep the main thread running with sleep and print "Main Thread" every 2 seconds
while print_line_thread.is_alive():
    print("Main Thread")
    time.sleep(2)

# Wait for the print_line_thread to complete
print_line_thread.join()

# Once printLine(9) is completed, print "All Done!"
print("All Done!")
