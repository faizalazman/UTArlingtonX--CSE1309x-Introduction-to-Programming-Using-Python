# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# While Loop, Exercise 3
# 0 points possible (ungraded)
# Write a program using while loop, which prints the sum of every third numbers from 1 to 1001 ( both 1 and 1001 are included)
# 
# (1 + 4 + 7 + 10 + ....)
# =============================================================================

# Type your code here
x = 1
num = 0
while x <= 1001:
     num += x
     x += 3        
print(num)