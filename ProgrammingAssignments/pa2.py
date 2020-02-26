# Ali Hooman
# alhooman@ucsc.edu
#
# Programming Assigment 2
# BMI Calculator
#
# BMI = (massKg) / (heightM**2)

print("**** BMI Calculator ****")

# Get weight in pounds
weightPounds = float(input("Your weight (pounds): "))

# Convert to kg ( 1 pound = 0.45 Kg )
massKg = weightPounds * 0.45

# Get height in inches
heightInches = float(input("Your height (inches): "))

# Convert to meters ( Divide by 39.37 )
heightMeters = heightInches / 39.37

# BMI = (massKg) / (heightM**2)
BMI = int( massKg / ( heightMeters**2 ) )

# Print BMI and health tip
if BMI < 18:
    print("BMI: ", BMI, ". You are underweight.", sep="")
elif BMI > 30:      
    print("BMI: ", BMI, ". You are overweight.", sep="")
else:
    print("BMI: ", BMI, ". Your weight is healthy.", sep="")
