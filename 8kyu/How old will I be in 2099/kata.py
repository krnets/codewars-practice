def calculate_age(year_of_birth, current_year):
    diff = current_year - year_of_birth

    if diff == 0:
        return 'You were born this very year!'
    elif diff == -1:
        return f'You will be born in 1 year.'
    elif diff < 1:
        return f'You will be born in {abs(diff)} years.'
    elif diff == 1:
        return f'You are 1 year old.'
    else:
        return f'You are {diff} years old.'