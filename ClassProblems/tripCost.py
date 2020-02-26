# Ali Hooman
# alhooman@ucsc.edu
#
# Class Problem: Calculate Trip Cost
#
# Ask user about total distance in miles, ask about MPG of
# vehicle, calculate total trip cost
# TripCost = (distance / mpg) * 2.59

distance = float(input("Trip distance: "))
milesPerGallon = float(input("Miles per gallon: "))
tripCost = ( distance / milesPerGallon ) * 2.59

print("Cost of trip is: $", round(tripCost, 2))

# Output:
# ali@eduroam-169-233-201-132:~/Brogramming/Python/CMPS-5P/ClassProblems$ !!
# python3 tripCost.py
# Trip distance: 100
# Miles per gallon: 10
# Cost of trip is: $ 25.9
