# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# # Conditional if elif, Exercise 5
# 0 points possible (ungraded)
#  Write a program which asks the user to type an integer.
# If the number is 2  then the program should print "two",
# If the number is 3  then the program should print "three",
# If the number is 5  then the program should print "five", 
# Otherwise it should print "other".
# =============================================================================

# Type your code here
data = int(input("Please type an integer: "))
if data == 2:
    print("two")
elif data == 3:
    print("three")
elif data == 5:
    print("five")
else:
    print("other")