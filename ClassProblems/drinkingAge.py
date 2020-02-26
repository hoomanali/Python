# Ali Hooman
# alhooman@ucsc.edu
#
# Legal Drinking Age
#
# Ask user for age, if age is unrealistic: error
# Print if they can drink or not
# Ask DOB and calculate age

age = input(int("What is your age: ")

if age < 0:
    print("Can't drink if you haven't been born yet.")
elif age > 150:
    print("Please input a realistic age.")
elif age < 21 and age > 0:
    print("You are not old enough to drink.")
elif age >= 21 and age < 150:
    print("You are old enough to drink.")
