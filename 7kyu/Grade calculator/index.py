""" 7kyu - Thinkful - List and Loop Drills: Grade calculator

You're a statistics professor and the deadline for submitting your students' grades is tonight at midnight. 
Each student's grade is determined by their mean score across all of the tests they took this semester.

You've decided to automate grade calculation by writing a function calculate_grade() that takes a list of 
test scores as an argument and returns a one character string representing the student's grade calculated as follows:

    90% <= mean score <= 100%: "A",
    80% <= mean score < 90%: "B",
    70% <= mean score < 80%: "C",
    60% <= mean score < 70%: "D",
    mean score < 60%: "F"

For example, calculate_grade([92, 94, 99]) would return "A" since the mean score is 95, 
and calculate_grade([50, 60, 70, 80, 90]) would return "C" since the mean score is 70.

Your function should handle an input list of any length greater than zero. """

from statistics import mean
# from bisect import bisect

# def calculate_grade(scores):
#     msc = mean(scores)
#     return 'A' if 90 <= msc <= 100 else 'B' if 80 <= msc <= 90 else 'C' if 70 <= msc <= 80 else 'D' if 60 <= msc <= 70 else 'F'

def calculate_grade(scores):
    msc = mean(scores)
    return 'ABCDF'[(msc < 90)+(msc < 80)+(msc < 70)+(msc < 60)]

# def calculate_grade(scores):
#     return 'FDCBA'[bisect([60, 70, 80, 90], mean(scores))]


q = calculate_grade([92, 94, 99]), "A"
q
q = calculate_grade([50, 60, 70, 80, 90]), "C"
q
q = calculate_grade([50, 55]), "F"
q
