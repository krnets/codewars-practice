""" 7kyu - Simple Fun #106: Is Thue Morse?

Given a sequence of 0s and 1s, determine if it is a prefix of Thue-Morse sequence.

The infinite Thue-Morse sequence is obtained by first taking a sequence containing a single 0 
and then repeatedly concatenating the current sequence with its binary complement.

A binary complement of a sequence X is a sequence Y of the same length such that the sum of 
elements X_i and Y_i on the same positions is equal to 1 for each i.

Thus the first few iterations to obtain Thue-Morse sequence are:

0
0 1
0 1 1 0
0 1 1 0 1 0 0 1
...

Examples

For seq=[0, 1, 1, 0, 1], the result should be true.

For seq=[0, 1, 0, 0], the result should be false.

    [input] integer array seq
    An non-empty array.

    Constraints:
    1 <= seq.length <= 1000
    seq[i] ∈ [0,1]

    [output] a boolean value
    true if it is a prefix of Thue-Morse sequence. false otherwise. """


# def is_thue_morse(seq):
#     res = [0]
#     for _ in range(int(len(seq)**0.5)+1):
#         res += [1 if int(x) == 0 else 0 for x in res]
#     return res[:len(seq)] == seq

# def is_thue_morse(seq):
#     return seq == [1 if bin(i).count('1') % 2 else 0 for i in range(len(seq))]

# def is_thue_morse(seq):
#     return all(bin(i).count('1') % 2 == n for i, n in enumerate(seq))

# def is_thue_morse(seq):
#     res = '0'
#     while len(res) < len(seq):
#         res += res.translate(str.maketrans('01', '10'))
#     return seq == list(map(int, res[:len(seq)]))

def is_thue_morse(seq):
    thue = [0]
    while len(thue) < len(seq):
        thue += [x ^ 1 for x in thue]
    return seq == thue[:len(seq)]


q = is_thue_morse([0, 1, 1, 0, 1]), True
q
q = is_thue_morse([0]), True
q
q = is_thue_morse([1]), False
q
q = is_thue_morse([0, 1, 0, 0]), False
q
