# def count_correct_characters(correct, guess):
#     if len(correct) != len(guess):
#         raise ValueError("lengths are different")
#     return sum(x == y for x, y in zip(correct, guess))


def count_correct_characters(correct, guess):
    assert len(correct) == len(guess)
    return sum(x == y for x, y in zip(correct, guess))
