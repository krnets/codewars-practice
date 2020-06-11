""" 6kyu - Turkish National Identity Number

Every Turkish citizen has an identity number whose validity can be checked by these set of rules:

    It is an 11 digit number
    First digit can't be zero
    Take the sum of 1st, 3rd, 5th, 7th and 9th digit and multiply it by 7.
    Then subtract the sum of 2nd, 4th, 6th and 8th digits from this value.
    Modulus 10 of the result should be equal to 10th digit.
    Sum of first ten digits' modulus 10 should be equal to eleventh digit.

Example:

10167994524
//  1+1+7+9+5= 23   // "Take the sum of 1st, 3rd, 5th, 7th and 9th digit..."
//    23 * 7= 161   //  "...and multiply it by 7"
//   0+6+9+4 = 19   // "Take the sum of 2nd, 4th, 6th and 8th digits..."
// 161 - 19 = 142   // "...and subtract from first value"
// "Modulus 10 of the result should be equal to 10th digit"
10167994524
         ^ = 2 = 142 % 10
// 1+0+1+6+7+9+9+4+5+2 = 44
// "Sum of first ten digits' modulus 10 should be equal to eleventh digit"
10167994524
          ^ = 4 = 44 % 10

Your task is to write a function to check the validity of a given number. Return true or false accordingly.
Note: The input can be a string in some cases. """


# def check_valid_tr_number(number):
#     str_n = str(number)

#     if not isinstance(number, int) or len(str_n) != 11 or str_n[0] == '0':
#         return False

#     nums13579mult7 = 7 * sum(int(str_n[i])
#                              for i in range(len(str_n)-1) if i % 2 == 0)

#     nums2468 = sum(int(str_n[i]) for i in range(len(str_n)-2) if i % 2)

#     mod10eq10th = int(str_n[9]) == (nums13579mult7 - nums2468) % 10

#     sum10mod10eq11th = sum(int(str_n[i]) for i in range(
#         len(str_n)-1)) % 10 == int(str_n[10])

#     return mod10eq10th and sum10mod10eq11th

# Take the sum of 1st, 3rd, 5th, 7th and 9th digit and multiply it by 7.
# Then subtract the sum of 2nd, 4th, 6th and 8th digits from this value.
# Modulus 10 of the result should be equal to 10th digit.
# Sum of first ten digits' modulus 10 should be equal to eleventh digit.


# def check_valid_tr_number(number):
#     str_n = str(number)

#     if not isinstance(number, int) or len(str_n) != 11 or str_n[0] == '0':
#         return False

#     return (7 * sum(map(int, str_n[:-1:2])) - sum(map(int, str_n[1:-2:2]))) % 10 == int(str_n[-2]) \
#         and sum(map(int, str_n[:10])) % 10 == number % 10


# def check_valid_tr_number(n):
#     return type(n) == int and len(str(n)) == 11 and 8 * sum(map(int, str(n)[:-1:2])) % 10 == sum(map(int, str(n)[:-1])) % 10 == n % 10

def check_valid_tr_number(number):
    number = str(number)

    if len(number) != 11 or not number.isdigit() or number[0] == '0':
        return False
        
    return str(sum(map(int, number[:-1])))[-1] == number[-1]

q = check_valid_tr_number(14352939209), False
q

q = check_valid_tr_number(10167994524), True  # 'A valid number'
q
# "should return false for numbers smaller than 11 digits"
q = check_valid_tr_number(6923522112), False
q
# "should return false for numbers bigger than 11 digits"
q = check_valid_tr_number(692352217312), False
q
# "should handle non-integer inputs"
q = check_valid_tr_number('x5810a78432'), False
q
q = check_valid_tr_number(36637640050), True  # 'A valid number'
q
q = check_valid_tr_number(12762438338), False  # 'An invalid number'
q
