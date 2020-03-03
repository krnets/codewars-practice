# 8kyu - Do I get a bonus?

""" It's bonus time in the big city! The fatcats are rubbing their paws in anticipation... but who is going to make the most money?

Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. 

If bonus is false, the fatcat did not make enough money and must receive only his stated salary.

Return the total figure the individual will receive as a string prefixed with "$" """


# def bonus_time(salary, bonus):
#     return '$' + (str(salary * 10) if bonus else str(salary))

# def bonus_time(salary, bonus):
#     return '$' + str(salary * [1, 10][bonus])

def bonus_time(salary, bonus):
    return '$' + str(salary * (10 if bonus else 1))

# def bonus_time(salary, bonus):
#     return f'${salary * (10 if bonus else 1)}'

# def bonus_time(salary, bonus):
#     return f'${salary * (1 +  bonus * 9)}'


q = bonus_time(10000, True)  # '$100000'
q
q = bonus_time(25000, True)  # '$250000'
q
q = bonus_time(10000, False)  # '$10000'
q
q = bonus_time(60000, False)  # '$60000'
q
q = bonus_time(2, True)  # '$20'
q
q = bonus_time(78, False)  # '$78'
q
q = bonus_time(67890, True)  # '$678900'
q
