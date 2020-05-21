# 8kyu - Age Range Compatibility Equation

""" Everybody knows the classic "half your age plus seven" dating rule that a lot of people 
follow (including myself). It's the 'recommended' age range in which to date someone.

minimum age <= your age <= maximum age #Task

Given an integer (1 <= n <= 100) representing a person's age, return their minimum and maximum age range.

This equation doesn't work when the age <= 14, so use this equation instead:

min = age - 0.10 * age
max = age + 0.10 * age

You should floor all your answers so that an integer is given instead of a float 
(which doesn't represent age). Return your answer in the form [min]-[max]

##Examples:

age = 27   =>   20-40
age = 5    =>   4-5
age = 17   =>   15-20 """


def dating_range(age):
    if age <= 14:
        min = age - 0.10 * age
        max = age + 0.10 * age
    else:
        min = age // 2 + 7
        max = (age - 7) * 2
    return f'{int(min)}-{int(max)}'

# def dating_range(age):
#     return '{}-{}'.format(int(age // 2 + 7 if age > 14 else age - 0.1 * age), int(2 * (age - 7) if age > 14 else age + 0.1 * age))


q = dating_range(17)  # "15-20"
q
q = dating_range(40)  # "27-66"
q
q = dating_range(15)  # "14-16"
q
q = dating_range(35)  # "24-56"
q
q = dating_range(10)  # "9-11"
q
