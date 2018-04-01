# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# Quiz 2 Part 5 (This Part has 1 Program)
# 10.0/10.0 points (graded)
# Write a program which asks the user to enter an integer 'n' which would be the total numbers of hours the user worked in a week and calculates and prints the total amount of money the user made during that week. If the user enters any number less than 0 or greater than 168 (n < 0 or n > 168) then your program should print INVALID 
# 
# Assume that hourly rate for the first 40 hours is $8 per hour. 
# 
# Hourly rate for extra hours between 41 and 50 (41 <= n <= 50 ) is $9 per hour. 
# 
# Hourly rate for extra hours greater than 50 is $10 per hour. 
# 
# Here are a few examples:
# 
# if the user enters -5, then your program should print
# INVALID
# if the user enters 34, then your program should print
# YOU MADE 272 DOLLARS THIS WEEK
# if the user enters 45, then your program should print
# YOU MADE 365 DOLLARS THIS WEEK
# if the user enters 67, then your program should print
# YOU MADE 580 DOLLARS THIS WEEK
# Note that the amount of money made by the user must be an integer (not a float) and your output should exactly match the format specified above (including spaces and capitalization).
# =============================================================================

# Type your code here
n = int(input("Number: "))
if n<0 or n>168:
    print("INVALID")
elif n<40:
    income = n*8
    print("YOU MADE {} DOLLARS THIS WEEK".format(income))
elif n >= 40 and n <=50:
    income = (n-40)*9 + (40*8)
    print("YOU MADE {} DOLLARS THIS WEEK".format(income))
else:
    income = (n-50)*10 +90 + 320
    print("YOU MADE {} DOLLARS THIS WEEK".format(income))