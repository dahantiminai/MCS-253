# QUESTION 1

print("LOAN REPAYMENT CALCULATOR\n")

class FinancialFun:
    
    def __init__(self, r, t, pv):
        self.r = r
        self.t = t
        self.pv = pv

    def rate(self):
        # calculate monthly interest rate
        rate = (self.r / 100) / 12
        return rate
    
    def timeperiod(self):
        # Calculate the total number of months
        timeperiod = self.t * 12
        return timeperiod
    

class PMT(FinancialFun):

    def calcPMT(self):
        # Use the rate and timeperiod methods from the parent class
        myrate = self.rate()
        mytimeperiod = self.timeperiod()
        
        # Calculate the PMT using the formula
        PMT = (self.pv * myrate) / (1 - (1 + myrate) ** -mytimeperiod)
        return PMT

# Take user input for interest rate, time period, and loan amount
interest_rate = float(input("Enter the interest rate (annual %): "))
time_period = float(input("Enter the time period (years): "))
loan_amount = float(input("Enter the loan amount: "))


# Create an instance of the PMT class and calculate the monthly payment
loan1 = PMT(interest_rate, time_period, loan_amount)  

result = loan1.calcPMT()
print(f"The monthly payment (PMT) is: K{result:.2f}")


# Case scenario:
# Mr. Max Tau wants to pay for a car so he decides to borrow from the bank. Mr. Tau
# gets a loan of K30,000, where the bank's annual interest rate is 10%. He must repay
# the loan in two years time, hence time repayment period is 2 years.

# What is the amount Mr. Tau will repay with interest, every month, until completion
# of the loan repayment after two years?

# interest_rate = 10%
# time_period = 2 years
# loan_amount = K30,000

# Therefore, the monthly payment that Mr. Tau will make (with interest)  for two years is: K1384.35



# QUESTION 2

# Part I

"""
Yes.

Becaue the attributes r, t, and pv are encapsulated within the FinancialFun class, 
and they are accessed or modified only through the class methods (rate and timeperiod).
However, the attributes are not private (e.g., they are not prefixed with an underscore), 
so they are not fully encapsulated.
"""

# Part II

"""
No, the code does not include polymorphism.

Polymorphism occurs when a method in a subclass overrides a method in its parent class or when the same method name 
is used in different classes to perform different tasks. In this code, the PMT class inherits from FinancialFun, 
but it does not override any methods from the parent class. Instead, it only uses the inherited methods (rate and timeperiod) 
without modifying their behavior.
"""

# Part III

"""
Yes, there is inheritance of attributes in the code.

The PMT class inherits from the FinancialFun class. This means that the PMT class automatically inherits the 
attributes r, t, and pv defined in the __init__ method of the FinancialFun class. These attributes are accessible 
in the PMT class without needing to redefine them. For example, the calcPMT method in the PMT class uses self.r, self.t, and self.pv, 
which are inherited from the FinancialFun class.
"""



# QUESTION 3

print()
print()
print("HYPOTENUSE CALCULATOR\n")

import math

lambda1 = lambda a, b: math.sqrt((a **2) + (b **2))

side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))

hypotenuse = lambda1(side_a, side_b)
print(f"The length of the hypotenuse is: {hypotenuse:.2f} units")


# The hypotenuse of a right triangle with sides a and b is given by the square root of the sum of the squares of the lengths 
# of the two sides, as given by the lambda function (line 108).
# Example: The hypotenuse of a right triangle with sides 3 and 4 is: 5.00 units