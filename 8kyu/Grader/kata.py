# def grader(score):
#     if score < 0.6 or score > 1:
#         return 'F'
#     elif score >= 0.9:
#         return 'A'
#     elif score >= 0.8:
#         return 'B'
#     elif score >= 0.7:
#         return 'C'
#     elif score >= 0.6:
#         return 'D'

def grader(score):
    grades = {.9: 'A', .8: 'B', .7: 'C', .6: 'D'}
    limit = 1.0

    for base, grade in grades.items():
        if base <= score <= limit:
            return grade

    return 'F'
