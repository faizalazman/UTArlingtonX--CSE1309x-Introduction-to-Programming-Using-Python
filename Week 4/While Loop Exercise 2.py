# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# While Loop, Exercise 2
# 0 points possible (ungraded)
# Write a program using while loop, which asks the user to type a positive integer, n, and then prints the factorial of n. A factorial is defined as the product of all the numbers from 1 to n (1 and n inclusive). For example factorial of 4 is equal to 24. (because 1*2*3*4=24)
# =============================================================================

# Type your code here
n = int(input("Number: "))
i = 1
count = 1
while i <= n:
    count = count*i
    i = i + 1
print(count)