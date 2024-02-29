import codewars_test as test
from kata import get_bingo_card

card = get_bingo_card()

def get_column(card, p):
    r=[]
    for i in card:
        if i[0]==p:
            r.append(i)
    return r

def get_column_order(card):
    r=''
    for i in card:
        if r=='' or r[-1]!=i[0]:
            r=r+i[0]
    return r
    
def numbers_are_in_range(column, min, max):
    for i in column:
        v = int(i[1:])
        if v < min or v > max:
            return False
    return True
    
def numbers_are_random(card):
    v = int(card[0][1:])
    for i in range(1,24):
        v1 = int(card[i][1:])
        if v1<v:
            return True
        v=v1
    return False
    

test.it("Bingo card:")

test.assert_equals(len(card), 24, "Has 24 numbers")
test.assert_equals(len(set(card)), 24, "Each number on card is unique")
test.assert_equals(len(get_column(card, 'B')), 5, "Column 'B' contains 5 items")
test.assert_equals(len(get_column(card, 'I')), 5, "Column 'I' contains 5 items")
test.assert_equals(len(get_column(card, 'N')), 4, "Column 'N' contains 4 items")
test.assert_equals(len(get_column(card, 'G')), 5, "Column 'G' contains 5 items")
test.assert_equals(len(get_column(card, 'O')), 5, "Column 'O' contains 5 items")
test.assert_equals(get_column_order(card), 'BINGO', "Numbers are ordered by column")
test.assert_equals(numbers_are_in_range(get_column(card, 'B'), 1, 15), True, "Numbers of column 'B' are between 1 and 15")
test.assert_equals(numbers_are_in_range(get_column(card, 'I'), 16, 30), True, "Numbers of column 'I' are between 16 and 30")
test.assert_equals(numbers_are_in_range(get_column(card, 'N'), 31, 45), True, "Numbers of column 'N' are between 31 and 45")
test.assert_equals(numbers_are_in_range(get_column(card, 'G'), 46, 60), True, "Numbers of column 'G' are between 46 and 60")
test.assert_equals(numbers_are_in_range(get_column(card, 'O'), 61, 75), True, "Numbers of column 'O' are between 61 and 75")
test.assert_equals(numbers_are_random(card), True, "Numbers are random within the columns")
