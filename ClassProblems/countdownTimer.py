# Ali Hooman
# alhooman@ucsc.edu
# Class problem 6 - countdown timer

import time

# Ask for number of seconds
seconds = input("Enter number of seconds: ")
sec = int(seconds)

# Count down from 0
for i in range(1, sec + 1):
    list[i] = 1
for j in reversed(list):

    # Print remaining seconds and wait 1 second
    time.sleep(1)
    print(j)

# Print final message after timer hits 0
print("0 seconds remaining")
