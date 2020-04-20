# 6kyu - Alien Beer Morse Code

""" The Earth has been invaded by aliens.
They demand our beer and threaten to destroy the Earth if we do not supply the exact number of beers demanded.

Unfortunately, the aliens only speak Morse code.
Write a program to convert morse code into numbers using the following convention:

1 .---- 2 ..--- 3 ...-- 4 ....- 5 ..... 6 -.... 7 --... 8 ---.. 9 ----. 0 ----- """

# def morse_converter(string):
#     n = 5
#     morse = ['-' * n]
#     for i in range(n):
#         num = list(morse[-1])
#         num[i] = '.'
#         morse.append(''.join(num))
#     morse += (''.join(x[::-1]) for x in morse[n-1:0:-1])
#     return int(''.join(str(morse.index(string[i:i+n])) for i in range(0, len(string), n)))

# def morse_converter(string):
#     n = 5
#     morse = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
#     return ''.join(str(morse.index(string[i:i+n])) for i in range(0, len(string), n))

# def morse_converter(string):
#     n, morse = 5, '-----#.----#..---#...--#....-#.....#-....#--...#---..#----.#'
#     return int(''.join(str(morse.find(string[i:i+n])//(n+1)) for i in range(0, len(string), n)))

# def morse_converter(string):
#     n, morse = 5, '-----  .----  ..---  ...--  ....-  .....  -....  --...  ---..  ----.'.split()
#     return int(''.join(str(morse.index(string[i:i+n])) for i in range(0, len(string), n)))

MORSE_NUM = {'-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
             '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}

def morse_converter(string):
    return int(''.join(MORSE_NUM.get(string[i:i+5]) for i in range(0, len(string), 5)))


q = morse_converter(".----")  # 1
q
q = morse_converter("..----------...")  # 207
q
q = morse_converter("----.--.....---...--")  # 9723
q
