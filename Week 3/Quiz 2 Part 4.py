# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# Quiz 2 Part 4 (This part has 1 Program)
# 10.0/10.0 points (graded)
# Write a program which asks the user to enter a positive integer 'n' (Assume that the user always enters a positive integer) and based on the following conditions, prints the appropriate results exactly as shown in the following format (as highlighted in yellow). 
# when 'n' is divisible by both 2 and 3 (for example 12), then your program should print
# BOTH
# when 'n' is divisible by only one of the numbers i.e divisible by 2 but not divisible by 3 (for example 8), or divisible by 3 but not divisible by 2 (for example 9), your program should print
# ONE
# when 'n' is neither divisible by 2 nor divisible by 3 (for example 25), your program should print
# NEITHER
# =============================================================================

# Type your code here
number = int(input("Please enter a number: "))
if (number%2 == 0) and (number%3 == 0):
    print("BOTH")
elif (number%2 == 0) or (number%3 == 0):
    print("ONE")
else:
    print("NEITHER")