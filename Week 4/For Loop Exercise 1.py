# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# For Loop, Exercise 1
# 0 points possible (ungraded)
# Using a for loop, write a program which prints the sum of all the even numbers from 1 to 101.
# =============================================================================

# Type your code here
count = 0
for i in range(1,101):
    if i % 2 == 0:
        count = count + i
print(count)    