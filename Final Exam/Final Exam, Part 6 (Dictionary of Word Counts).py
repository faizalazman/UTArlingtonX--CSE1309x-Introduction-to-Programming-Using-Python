# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 14:09:21 2018

@author: Parmenides
"""

# =============================================================================
# Final Exam, Part 6 (Dictionary of word counts)
# 20.0/20.0 points (graded)
# Write a function that takes a string of words as input argument and returns a dictionary of word counts. The keys of this dictionary should be the unique words and the values should be the total count of those words. Assume that characters are not case sensitive. For example if the input string is :
# 
# "I am tall when I am young and I am short when I am old" 
# Then the output should be:
# {'short': 1, 'young': 1, 'am': 4, 'when': 2, 'tall': 1, 'i': 4, 'and': 1, 'old': 1} 
# =============================================================================

# Type your code here
def word_counter(my_string):
    my_string = my_string.lower().split()
    count = dict()
    
    for word in my_string:
        if word in count:
            count[word]+= 1
        else:
            count[word] = 1
            
    return count