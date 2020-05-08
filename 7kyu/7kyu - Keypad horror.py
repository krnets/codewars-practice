# 7kyu - Keypad horror

""" Having two standards for a keypad layout is inconvenient! Computer keypad's layout:
7 8 9 \n 4 5 6 \n 1 2 3 \n 0 \n

Cell phone keypad's layout:
1 2 3\n 4 5 6\n 7 8 9\n 0\n

Solve the horror of unstandartized keypads by providing a function that converts computer input 
to a number as if it was typed by a phone.

Example:
"789" -> "123"

Notes:
You get a string with numbers only """


def computer_to_phone(numbers):
    return numbers.translate(str.maketrans('123789', '789123'))

q = computer_to_phone("0789456123"), "0123456789"
q
q = computer_to_phone("000"), "000"
q
q = computer_to_phone("94561"), "34567"
q