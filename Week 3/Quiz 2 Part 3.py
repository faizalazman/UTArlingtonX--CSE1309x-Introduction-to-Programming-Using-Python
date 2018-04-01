# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# Quiz 2 Part 3 (This part has 1 Program)
# 10.0/10.0 points (graded)
# Write a program which asks the user to enter their age in years (Assume that the user always enters an integer) and based on the following conditions, prints the output exactly as in the following format (as highlighted in yellow): 
# When age is less than or equal to 0, your program should print
# UNBORN
# When age is greater than 0 and less than or equal to 150, your program should print
# ALIVE
# When age is greater than 150, your program should print
# VAMPIRE
# Note that your printed output should be in capital letters and there should be no extra spaces.
# =============================================================================

# Type your code here
data = int(input("Please input your age: "))
if data <= 0:
    print("UNBORN")
elif data > 0 and data <= 150:
    print("ALIVE")
else:
    print("VAMPIRE")