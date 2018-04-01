# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 14:09:21 2018

@author: Parmenides
"""

# =============================================================================
# Final Exam, Part 4 (Calculate your grade for this course)
# 20.0/20.0 points (graded)
# Write a function named my_final_grade_calculation that receives a file name and returns a dictionary that tells whether a student in this course passed or failed based on the following criteria. 
# 
# Each line of the file will have the format:
# 
# name, q1, q2, q3, q4, q5, q6, a1, a2, a3, a4, midterm, final
# where
# name is a string
# q1 through q6 are quiz scores (integers)
# a1 through a4 are assignment scores (integers values)
# midterm is midterm score (integer)
# final is final exam score (integer)
# For example, if the content of the file looks like this:
# tom, 10, 20, 0, 100, 0, 100, 70, 80, 90, 0, 80, 85
# mary, 0, 50, 66, 40, 10, 60, 70, 80, 90, 100, 80, 85
# joan, 0, 80, 40, 10, 50, 60, 7, 80, 90, 0, 80, 5
# Note that there may be additional spaces between the entries in each line. 
# 
# Your function should return a dictionary such as:
# {"tom":"pass", "mary":"pass", "joan":"fail"} 
# Notes:
# Two of the lowest quizzes should be dropped and the average of the remaining four quizzes is worth 25% of the total grade.
# The lowest assignment score should be dropped and the average of the remaining three assignments is worth 25% of the total grade.
# Midterm and final exams are each 25% of the total grade.
# Calculate the total score of the student and if the total score is greater than or equal to 60 (totalscore >= 60) then the student has passed. Notice that the keys (names) and the values (pass or fail) of the dictionary should be all lower cased with no spaces in any of them.
# =============================================================================

# Type your code here
def my_final_grade_calculation(filename):
    file = open(filename,'r').read().strip().replace(",","").split()
    keys = []
    for i in range(0,len(file),13):
        keys.append(file[i])
    for word in file:
        if word in keys:
            file.remove(word)
            
    file = list(map(int,file))
##########################################################################            
    quizes = []
    for i in range(0,len(file),12):
            value = file[i:i+6]
            quizes.append(value)
    for quiz in quizes:
        quiz.sort(reverse = True)
        del quiz[4:6]
    quizy = []
    for quiz in quizes:
        average = sum(quiz)/len(quiz)
        quizy.append(average)
##########################################################################        
    assignments = []
    for i in range(6,len(file),12):
            value_ass = file[i:i+4]
            assignments.append(value_ass)
    for assignment in assignments:
        assignment.sort(reverse = True)
        del assignment[3]
    total = []
    for assignment in assignments:
        average = sum(assignment)/len(assignment)
        total.append(average)
##########################################################################
    exams = []
    for i in range(10,len(file),12):
        value_exam = file[i:i+2]
        exams.append(value_exam)
    total_exams = []
    for exam in exams:
        exam = sum(exam)
        total_exams.append(exam)
##########################################################################
    scores = []
    for i in range(len(total)):
        score = (total[i] + total_exams[i] + quizy[i])/4
        scores.append(score)
        
    for i in range(0,len(scores)):
        if scores[i] >= 60:
            scores[i] = 'pass'
        else:
            scores[i] = 'fail'
            
    return dict(zip(keys,scores))
