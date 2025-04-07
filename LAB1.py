# MCS 253 Week 4 Session 2
# Topic: Functions

# Group Members: 
# Dahan Timinai
# Natasha Ricky 
# Rophie Nomoru

"""
# Task 1: Create a function that calculates the area of a rectangle.
def rect_area(length, width):

    area = length * width

    return area

result = rect_area(10, 5)

print("The area of the rectangle is", result, "square units.")
"""


"""
# Task 2: Create a function that calculates the perimeter of a rectangle.
def rect_perimeter(length, width):

    perimeter = ((length * 2) + (width * 2))

    return perimeter

result = rect_perimeter(10, 5)

print("The perimeter of the rectangle is", result, "units.")
"""

"""
# Task 3: Create a function that takes user input for length and width, and returns the area and perimeter of the rectangle based on user input.

# Ask for user input
length = float(input("what is the length of the rectangle?\n"))
width = float(input("what is the width of the rectangle?\n"))

# Function to calculate the area of a rectangle
def rect_area(length, width):

    area = length * width

    return area

# Function to calculate the perimeter of a rectangle
def rect_perimeter(length, width):

    perimeter = (length * 2) + (width * 2)

    return perimeter


area = rect_area(length, width)
print("The area of the rectangle is", area, "square units.")

perimeter = rect_perimeter(length, width)
print("The perimeter of the rectangle is", perimeter, "units.")
"""


#Task 4 (Lab 1): Create a function that takes user input for length and width, and returns the area or perimeter of the rectangle based on user choice.

# Function to calculate the area of a rectangle
def rect_area(length, width):

    area = length * width

    return area



# Function to calculate the perimeter of a rectangle
def rect_perimeter(length, width):

    perimeter = (length * 2) + (width * 2)

    return perimeter


print("Welcome, user. I am a Rectanle Perimeter and Area calculator.\n")

# Ask for user input
userchoice = input("To calcualte the area of a rectangle, enter 1.\nTo calculate the perimeter of a rectangle, enter 2.\n")

# Check user choice and call the appropriate function
if userchoice == "1":

    print("Great! You want to calculate the area of a rectangle!\n")

    length = float(input("What is the length of the rectangle?\n"))
    width = float(input("What is the width of the rectangle?\n"))

    area = rect_area(length, width)
    print("The area of the rectangle is", area, "square units.")

elif userchoice == "2":

    print("Awesome! You want to calculate the perimeter of a rectangle!\n")

    length = float(input("What is the length of the rectangle?\n"))
    width = float(input("What is the width of the rectangle?\n"))

    perimeter = rect_perimeter(length, width)
    print("The perimeter of the rectangle is", perimeter, "units.")

else:

    print("Invalid choice. Please enter 1 or 2.")
