# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:33:45 2018

@author: Parmenides
"""


# =============================================================================
# Final Exam, Part 3 (N letter dictionary)
# 20.0/20.0 points (graded)
# Write a function named n_letter_dictionary that receives a string (words separated by spaces) as parameter and returns a dictionary whose keys are numbers and whose values are lists that contain unique words that have the number of letters equal to the keys. 
# 
# For example, when your function is called as:
# 
# n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become")
# Then, your function should return a dictionary such as
# {2: ['is'], 3: ['and', 'see', 'the', 'way', 'you'], 4: ['them', 'they', 'what'], 5: ['treat'], 6: ['become', 'people']}
# Notes:
# Each list of words with the same number of letters should be sorted in ascending order
# The words in a list should be unique. For example, even though the word "them" is repeated twice in the above sentence, it is only considered once in the list of four letter words.
# Capitalization does not matter, this means that all the words should be converted to lower case. For example the words "The" and "the" appear in the sentence but they are both considered as lower case "the".
# =============================================================================

# Type your code here
def n_letter_dictionary(my_string):
    strings = my_string.lower().split()
    count_string = []
    for string in strings:
        length = len(string)
        count_string.append(length)
    strings = sorted(list(set(strings)))
    count_string = list(set(count_string))
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    l8 = []
    l9 = []
    l10 = []
    for word in strings:
        if len(word) == 1:
            l1.append(word)
        elif len(word) == 2:
            l2.append(word)
        elif len(word) == 3:
            l3.append(word)
        elif len(word) == 4:
            l4.append(word)
        elif len(word) == 5:
            l5.append(word)
        elif len(word) == 6:
            l6.append(word)
        elif len(word) == 7:
            l7.append(word)
        elif len(word) == 8:
            l8.append(word)
        elif len(word) == 9:
            l9.append(word)
        else:
            l10.append(word)
    full = list((l1,l2,l3,l4,l5,l6,l7,l8,l9,l10))
    full_total = []
    for li in full:
        if len(li) == 0:
            continue
        else:
            full_total.append(li)

    return dict(zip(count_string, full_total))