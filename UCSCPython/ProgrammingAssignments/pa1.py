# Ali Hooman
# alhooman@ucsc.edu
#
# Convert Fahrenheit to Celsius
# C = (F - 32) * (5/9)

# Get temp in Fahrenheit
tempF = float(input("Enter temperature in Fahrenheit: "))

# Convert to C
tempC = (tempF - 32) * (5/9)

# Print Temp in Celsius
print(round(tempF,2), "F in Celsius is:", round(tempC, 2), "C")

# Output:
# ali@MBAir:~/Brogramming/Python/CMPS-5P/ProgrammingAssignments$ !!
# python3 pa1.py
# Enter temperature in Fahrenheit: 22.34534623423
# 22.35 F in Celsius is: -5.36 C
