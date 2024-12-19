# Ali Hooman
# alhooman@ucsc.edu
# Class assignment 7
# sum of natural numbers

# Ask user to input upper limit n

n = int(input("Enter a natural number"))

aSum = 0

# use for loop and accumulator to calc some of 1 to n
for i in range (1,n+1):
    aSum = aSum + i

print("Total sum is: ")
print(aSum)

