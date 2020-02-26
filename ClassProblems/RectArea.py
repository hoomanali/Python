#
# Ali Hooman
# alhooman@ucsc.edu
# Class Problem 2 - Area of Rectangle
#
# Ask user for inputs for height and width.
# Calculate area of rectangle and print the result
# Calculate circumference
# 

# Get height
heightStr = input("Enter height: ")
heightInt = int(heightStr)

# Get width
widthStr = input("Enter width: ")
widthInt = int(widthStr)

# Output area (width * height)
area = heightInt * widthInt
print("Area is ", area)

# Output circumference ( 2*(width + height) )
circumference = 2 * ( widthInt + heightInt )
print("Circumference is ", circumference)

# Output:
# ali@eduroam-169-233-227-170:~/Brogramming/Python/CMPS-5P/ClassProblems$ !!
# python3 RectArea.py
# Enter height: 2
# Enter width: 4
# Area is  8
# Circumference is  12
