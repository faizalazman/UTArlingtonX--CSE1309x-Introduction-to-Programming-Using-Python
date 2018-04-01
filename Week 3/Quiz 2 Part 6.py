# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# Quiz 2 Part 6 (This Part has 1 Program)
# 10.0/10.0 points (graded)
# Write a program that asks the user to enter a positive integer n. Assuming that this integer is in seconds, your program should convert the number of seconds into days, hours, minutes, and seconds and prints them exactly in the format specified below. Here are a few sample runs of what your program is supposed to do: 
# 
# when user enters
# 
# 369121517
# your program should print:
# 4272 days 5 hours 45 minutes 17 seconds
# when user enters
# 24680
# your program should print:
# 0 days 6 hours 51 minutes 20 seconds
# when user enters
# 129600
# your program should print:
# 1 days 12 hours 0 minutes 0 seconds
# Note that the numbers and words in the above output are separated by only one space. All the words are in lower case. Your output should exactly match the format shown above.
# =============================================================================

# Type your code here
time = int(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("{} days {} hours {} minutes {} seconds".format(day, hour, minutes, seconds))