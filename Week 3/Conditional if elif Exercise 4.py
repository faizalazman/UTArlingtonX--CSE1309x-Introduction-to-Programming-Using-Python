# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""

# =============================================================================
# Conditional if elif, Exercise 4
# 0 points possible (ungraded)
#  Write a program which asks the user to type a string and then: 
# Print "Dog" if the word "dog" exists in the input string.
# Print "Cat" if the word "cat" exists in the input string. (if both "dog" and "cat" exist in the input string, then you should only print "Dog") 
# Otherwise prints "None". (Pay attention to capitalization).
# =============================================================================

# Type your code here
data = input("Please type a sentence with an animal in it: ")
if "dog" in data:
    print("Dog")
elif "cat" in data:
    print("Cat")
else:
    print("None")