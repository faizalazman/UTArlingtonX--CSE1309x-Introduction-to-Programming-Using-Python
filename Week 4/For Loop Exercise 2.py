# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# For loop, Exercise 2
# 0 points possible (ungraded)
# Using a for loop, write a program which asks the user to type an integer, n, and then prints the sum of all numbers from 1 to n (including both 1 and n).
# =============================================================================

# Type your code here
number = int(input("Number: "))
count = 1
for i in range(1,number):
    count = count + i + 1
print(count)