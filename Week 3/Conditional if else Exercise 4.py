# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""

# =============================================================================
# Conditional if else, Exercise 4
# 0 points possible (ungraded)
# Write a program which asks the user to type an integer and then prints "Yes" if that integer is divisible by 3, otherwise prints "No"
# =============================================================================

# Type your code here
data = int(input("Please input a number: "))
if data % 3 == 0:
    print("Yes")
else:
    print("No")
