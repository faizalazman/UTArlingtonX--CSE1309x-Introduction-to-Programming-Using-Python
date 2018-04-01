# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""

# =============================================================================
# Part 3 (This part has 1 Program)
# 10.0/10.0 points (graded)
# Write a program that asks the user to enter their age in years as input (assume that the user enters a positive integer) and calculates and prints how old the user is in terms of days. Assume that there are 365 days in a year. For example: if the user enters
# 
# 22
# then your program should print
# You are 8030 days old
# Pay attention to the spaces. In order to receive proper grade, your output should EXACTLY match the output shown in the sample solution (highlighted in yellow) including spaces and capitalization.
# =============================================================================


# Type your code here
year = int(input("Please enter your age : "))
days_age = year * 365
print("You are {} days old".format(days_age))

