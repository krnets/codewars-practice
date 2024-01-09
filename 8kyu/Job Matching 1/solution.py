# def match(candidate, job):
#     if 'min_salary' not in candidate:
#         raise ValueError('Minimum salary not specified')
#     if 'max_salary' not in job:
#         raise ValueError('Maximum salary not specified')

#     return job['max_salary']>= candidate['min_salary'] * 0.9

def match(candidate, job):
    return job['max_salary'] >= candidate['min_salary'] * 0.9
