# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""

# =============================================================================
# Part 5 (This Part Has 1 Program)
# 10.0/10.0 points (graded)
# Write a program that asks the user for a positive integer between 1 and 7 (Assume that the user may enter any number from 1 to 7 both inclusive) and prints the day of week corresponding to that number in all capital letters. Assume that the day of the week starts from MONDAY. For example: if the user enters:
# 
# 2
# then your program should print
# TUESDAY
# if the user enters
# 5
# then your program should print
# FRIDAY
# 
# etc. Do NOT use shortcut names for the days of the weeks like "tue" or "fri". The names have to be completely spelled in Capital lettets. Hint: Use a list containing days of the week.
# Pay attention to the spaces. In order to receive proper grade, your output should EXACTLY match the output shown in the sample solution (highlighted in yellow) including spaces and capitalization.
# 
# =============================================================================

# Type your code here

day = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
inpt = int(input("Give me an integer between 1 and 7: "))
print(day[inpt - 1])


