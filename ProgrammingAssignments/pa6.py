# Ali Hooman
# alhooman@ucsc.edu
#
# Programming Assignment 6
# Calculate letter grades based on exam scores 

import math

# Read list of exam scores from input
# Scores entered as single list separated by commas
grades = input("Enter grades separated by commas: ")

# Convert string to list
gradesList = grades.split(",")

# Convert list elements to int
for i in range(len(gradesList)):
    gradesList[i] = int(gradesList[i])

# Calculate mean
# mean = ( x1 + x2 + x3 ... + xn ) / n
# n = length of list
n = len(gradesList)

meanSum = 0
for grade in gradesList:
    meanSum += grade

mean = meanSum / n
print("Mean:", round(mean,2))

# Calculate standard deviation
# stdDev = sqrt( (x1-mean)**2 + (x2-mean)**2 +...+ (xn-mean)**2 ) / n )
stdDev = 0

for grade in gradesList:
    stdDev += ((grade-mean)**2)
    stdDev = stdDev / n
    stdDev = math.sqrt(stdDev)
print("Standard deviation:", round(stdDev,2))

# Assign letter grades based on mean and stDev
print("Grades: ", sep = " ", end = "")
for i in range(len(gradesList) + 1):
    # A >= mean + 1.5(stdDev)
    if gradesList[i-1] >= (mean + 1.5 * (stdDev)):
        print("A", sep="", end="")
    # B < mean + 1.5(stdDev) and , sep="", end=""B >= mean + 0.5(stdDev)
    elif gradesList[i-1] < (mean + 1.5 * (stdDev)) and gradesList[i-1] >= (mean + 0.5 * (stdDev)):
        print("B", sep="", end="")
    # C < mean + 0.5(stdDev) and C >= mean - 0.5(stdDev)
    elif gradesList[i-1] < (mean + 0.5 * (stdDev)) and gradesList[i-1] >= (mean - 0.5 * (stdDev)):
        print("C", sep="", end="")
    # D < mean - 0.5(stdDev) and D >= mean - 1.5(stdDev) 
    elif gradesList[i-1] < (mean - 0.5 * (stdDev)) and gradesList[i-1] >= (mean - 1.5 * (stdDev)):
        print("D", sep="", end="")
    # F < mean - 1.5(stdDev)
    elif gradesList[i-1] < (mean - 1.5 * (stdDev)):
        print("F", sep="", end="")
    
    if (i) < len(gradesList):
        print(",", sep="", end="")
print()
