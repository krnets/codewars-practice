# def HQ9(code):
#     def rec(bottles, res):
#         if bottles == 0:
#             res += "No more bottles of beer on the wall, no more bottles of beer.\n" + \
#                 "Go to the store and buy some more, 99 bottles of beer on the wall."
#             return res
#         elif bottles == 1:
#             res += "1 bottle of beer on the wall, 1 bottle of beer.\n" + \
#                 "Take one down and pass it around, no more bottles of beer on the wall.\n"
#         elif bottles == 2:
#             res += "2 bottles of beer on the wall, 2 bottles of beer.\n" + \
#                 "Take one down and pass it around, 1 bottle of beer on the wall.\n"
#         else:
#             res += f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.\n"
#             res += f"Take one down and pass it around, {bottles-1} bottles of beer on the wall.\n"
#         return rec(bottles-1, res)

#     ans = ''

#     match code:
#         case 'H': ans = 'Hello World!'
#         case 'Q': ans = code
#         case '9': ans = rec(99, ans)
#         case _: return None

#     return ans

LINE = '{0} of beer on the wall, {0} of beer.\nTake one down and pass it around, {1} of beer on the wall.'

SONG = '\n'.join(LINE.format(f'{i} bottles',
                             f'{i - 1} bottle' + 's' * (i > 2))
                 for i in reversed(range(2, 100))) + \
    """
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall."""


def HQ9(code):
    match code:
        case 'H': return 'Hello World!'
        case 'Q': return code
        case '9': return SONG
        case _: return None
