# 8kyu - Fake Binary

""" Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. 
Return the resulting string. """


# def fake_bin(x):
#     return (str([1 if int(i) >= 5 else 0 for i in list(x)])).replace(', ', '')[1:-1]

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)


q = fake_bin("45385593107843568")  # "01011110001100111"
q
q = fake_bin("509321967506747")  # "101000111101101"
q
q = fake_bin("366058562030849490134388085")  # "011011110000101010000011011"
q
q = fake_bin("15889923")  # "01111100"
q
q = fake_bin("800857237867")  # "100111001111"
q
