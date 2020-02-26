# Ali Hooman
# alhooman@ucsc.edu
# Lottery

import random
import time

# Ask user to guess number between 1 and 10 inclusive
userGuess = input("Guess a number from 1 to 10: ")
print("Your guess: ")
print(userGuess)

# Generate ran in range
randNum = random.randrange(1, 11, 1)

# Wait 3 seconds with sleep function from the time module
time.sleep(3)

# Print rand
print("Number is: ", randNum)

# Check if guess is correct and print
if userGuess == randNum:
    print("You are correct!")
else:
    print("Wrong guess.")
