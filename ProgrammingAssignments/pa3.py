# Ali Hooman
# alhooman@ucsc.edu
#
# Programming Assignment 3
# The Law of Large Numbers
import random

# Get total number of experiments (n)
n = int(input("How many experiments? "))
totalSum = 0

# Perform n experiments
for i in range(1, n+1):
    # Generate rand [1,6] using randrange
    totalSum = totalSum + random.randrange(1,6)

# Sum all rand numbers, divide by n for avg
average = totalSum / n
# Expected value is mu == 3.5

# Print overall average
print("Average is:", average)
