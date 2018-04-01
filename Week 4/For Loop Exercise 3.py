# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# For Loop, Exercise 3
# 0 points possible (ungraded)
# Using a for loop, write a program which asks the user to type a positive integer, n, and then prints the sum of the square of all numbers form 1 to n (including both 1 and n).
# 
# For example if the user type 3, the answer should be ((3**2) + (2**2) + (1**2)) = 14
# =============================================================================

# Type your code here
n = int(input("Number: "))
total = 0
for i in range(1,n + 1):
    number = i**2
    total = total + number
print(total)