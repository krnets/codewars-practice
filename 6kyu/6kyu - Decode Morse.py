# 6kyu - Decode Morse

""" Oh no! You have stumbled upon a mysterious signal consisting of beeps of various lengths, 
and it is of utmost importance that you find out the secret message hidden in the beeps. 
There are long and short beeps, the longer ones roughly three times as long as the shorter ones. Hmm... that sounds familiar.

That's right: your job is to implement a decoder for the Morse alphabet. 
Rather than dealing with actual beeps, we will use a common string encoding of Morse. 
A long beep is represened by a dash (-) and a short beep by a dot (.). 
A series of long and short beeps make up a letter, and letters are separated by spaces (). 
Words are separated by double spaces.

You should implement the International Morse Alphabet. You need to support letters a-z and digits 0-9 as follows:

a .-      h ....    o ---     u ..-      1 .----     6 -....
b -...    i ..      p .--.    v ...-     2 ..---     7 --...
c -.-.    j .---    q --.-    w .--      3 ...--     8 ---..
d -..     k -.-     r .-.     x -..-     4 ....-     9 ----.
e .       l .-..    s ...     y -.--     5 .....     0 -----
f ..-.    m --      t -       z --..
g --.     n -.

Examples

.... . .-.. .-.. ---  .-- --- .-. .-.. -..   → "hello world"
.---- ... -  .- -. -..  ..--- -. -..         → "1st and 2nd"

A dictionnary TOME is preloaded for you, with the information above to convert morse code to letters. """

# TOME preloaded

TOME = {'...': 's', '..-': 'u', '-.': 'n', '-..-': 'x', '.----': '1', '-': 't', '.--.': 'p', '.---': 'j', '....-': '4', '.-.': 'r', '.....': '5', '-----': '0', '-...': 'b', '-..': 'd', '----.': '9', '-....': '6', '--.-': 'q', '--..': 'z',
        '.--': 'w', '---': 'o', '..---': '2', '.-': 'a', '..': 'i', '-.-.': 'c', '...--': '3', '-.--': 'y', '....': 'h', '---..': '8', '...-': 'v', '--...': '7', '--.': 'g', '.': 'e', '--': 'm', '.-..': 'l', '..-.': 'f', '-.-': 'k'}


# def decode(s):
#     words = s.replace('  ', '|').split('|')
#     # return ''.join(TOME[x] if x is not '' else ' ' for x in s.split())
#     # return ''.join(TOME[x] if x is not '' else ' ' for x in words)
#     # return ' '.join(map(lambda word: TOME[x] for x in list(words), words))
#     # return '|||'.join(map(lambda word: ''.join(TOME[x] for x in word), words))
#     res = []
#     # for word in words:
#     # res.append(word)
#     # return res
#     # return ''.join(TOME[x] for x in words[0].split())
#     return ' '.join(map(lambda word: ''.join(TOME[x] for x in word.split()), words))

# def decode(s):
#     words = s.replace('  ', '|').split('|')
#     return ' '.join(map(lambda word: ''.join(TOME[x] for x in word.split()), words))

# def decode(s):
#     return ' '.join(map(lambda word: ''.join(TOME[x] for x in word.split()), s.split('  ')))

def decode(s):
    return '' if not s else ''.join(TOME.get(x, ' ') for x in s.split(' '))


q = decode(".... . .-.. .-.. ---  .-- --- .-. .-.. -..")  # "hello world"
q
q = decode(".---- ... -  .- -. -..  ..--- -. -..")  # "1st and 2nd"
q
q = decode("..  .- --  .-  - . ... -")  # "i am a test"
q
q = decode(".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.. ----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.")
q
#                     "abcdefghijklmnopqrstuvwxyz0123456789", "Double-check that you cover the entire required alphabet"
q = decode("")  # ""
q
