# 7kyu - Bits Battle

""" The odd and even numbers are fighting against each other!

You are given a list of positive integers. 
The odd numbers from the list will fight using their 1 bits from their binary representation, 
while the even numbers will fight using their 0 bits. If present in the list, number 0 will be neutral, hence not fight for either side.

You should return:

    odds win if number of 1s from odd numbers is larger than 0s from even numbers
    evens win if number of 1s from odd numbers is smaller than 0s from even numbers
    tie if equal, including if list is empty

Please note that any prefix that might appear in the binary representation, e.g. 0b, should not be counted towards the battle.
Example:

For an input list of [5, 3, 14]:

    odds: 5 and 3 => 101 and 11 => four 1s
    evens: 14 => 1110 => one 0

Result: odds win the battle with 4-1 """

# def bits_battle(numbers):
#     odds = sum(bin(x)[2:].count('1') for x in numbers if x % 2 != 0)
#     evens = sum(bin(x)[2:].count('0') for x in numbers if x % 2 == 0)
#     if odds > evens: return 'odds win'
#     elif odds < evens: return 'evens win'
#     else: return 'tie'

# def bits_battle(numbers):
#     odds = sum(bin(x)[2:].count('1') for x in numbers if x % 2 != 0)
#     evens = sum(bin(x)[2:].count('0') for x in numbers if x % 2 == 0)
#     return 'odds win' if odds > evens else 'evens win' if odds < evens else 'tie'


def bits_battle(numbers):
    odds = sum(bin(x).count('1') for x in numbers if x % 2 != 0)
    evens = sum(bin(x).count('0') - 1 for x in numbers if x % 2 == 0)
    return 'odds win' if odds > evens else 'evens win' if odds < evens else 'tie'


q = bits_battle([5, 3, 14])  # 'odds win'
q
q = bits_battle([3, 8, 22, 15, 78])  # 'evens win'
q
q = bits_battle([])  # 'tie'
q
q = bits_battle([1, 13, 16])  # 'tie'
q
