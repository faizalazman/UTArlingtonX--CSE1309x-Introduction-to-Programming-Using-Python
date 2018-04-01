# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# For Loop Exercise 4
# 0 points possible (ungraded)
# Write a program that asks the user for an input 'n' (assume that the user enters a positive integer) and prints a sequence of powers of 10 from 10^0 to 10^n in separate lines. For example if 'n' is equal to 4 then the output should look like the following:
# 
# 1
# 10
# 100
# 1000
# 10000
# =============================================================================

# Type your code here
n = int(input("Number: "))
for i in range(0, n + 1):
    square = 10**i
    print(square)