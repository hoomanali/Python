# Ali Hooman
# alhooman@ucsc.edu
#
# Programming Assignment 4
# Savings account - manages savings account for 1 year
# with monthly interest rates, deposits, and withdrawals.

print("******Savings Account******")

# Get initial deposit and annual interest rate
a = float(input("Enter the initial deposit: "))

r = float(input("Enter the annual rate (0-100): "))

while r < 0 or r > 100:
    r = float(input("Invalid rate, enter annual rate (0-100): "))

# Loop through each month
for month in range(1,13):
    
    print("Month: ", month)
    print("Balance: ", "%.2f" % a)

    # Ask for:
    # d, deposit
    # w, withdrawal
    d = float(input("Enter this month's deposit: "))

    w = float(input("Enter this month's withdrawal: "))

    if w > a:
        print("Insufficient funds.")
        w = 0

    # Calculate aNew using aPrev and monthly compounding rate.
    #   a = ( a * ( 1 + (1/12) * (r/100) ) ) + d - w
    #   Print new balance
    a = ( a * ( 1 + (1/12) * (r/100) ) ) + d - w

print("Final Balance: ", "%.2f" % a)
