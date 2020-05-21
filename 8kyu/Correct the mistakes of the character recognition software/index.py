# 8kyu - Correct the mistakes of the character recognition software

""" Character recognition software is widely used to digitise printed texts. 
Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised 
character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

    S is misinterpreted as 5
    O is misinterpreted as 0
    I is misinterpreted as 1

The test cases contain numbers only by mistake. """


# def correct(string):
#     return string.replace('0', 'O').replace('1', 'I').replace('5', 'S')

def correct(string):
    return string.translate(string.maketrans('501', 'SOI'))


q = correct("L0ND0N")  # "LONDON"
q
q = correct("DUBL1N")  # "DUBLIN"
q
q = correct("51NGAP0RE")  # "SINGAPORE"
q
q = correct("BUDAPE5T")  # "BUDAPEST"
q
q = correct("PAR15")  # "PARIS"
q
