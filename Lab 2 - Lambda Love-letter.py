# lambda function to convert hours to days
convert_to_days = lambda hours: hours/24

# Take user input
hours = float(input("Enter value in hours: "))

# Call function and print output
days = convert_to_days(hours)
print(f"{hours} hours equals {days} days.")

# Alternatively, call the function directly within the print statement
# print(f"{hours} hours equals {convert_to_days(hours)} days.")