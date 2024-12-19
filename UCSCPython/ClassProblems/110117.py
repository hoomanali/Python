# Ali Hooman
# alhooman@ucsc.edu
#
# Class Problem 12: Fizz Buzz
#
# prints numbers from 1 to 100
# For multiples of 3, print Fizz.
# For multiples of 5, print Buzz.
# for both, print FizzBuzz.

for i in range(1,101):

    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
