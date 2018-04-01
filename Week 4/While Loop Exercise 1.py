# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# WHILE LOOP, EXERCISE 1
# 0 points possible (ungraded)
# Write a program which prints the sum of numbers from 1 to 101 that are divisible by 5. ( 1 and 101 are included) (Use while loop)
# =============================================================================

# Type your code here
x=0 
count=0 
while x<=100: 
    if x%5==0: 
        count=count+x 
    x=x+1 
print(count) 