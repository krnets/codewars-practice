# 6kyu - Drunk friend

""" You're hanging out with your friends in a bar, when suddenly one of them is so drunk, that he can't speak, 
and when he wants to say something, he writes it down on a paper. However, none of the words he writes make sense to you. 
He wants to help you, so he points at a beer and writes "yvvi". You start to understand what he's trying to say, 
and you write a script, that decodes his words.

Keep in mind that numbers, as well as other characters, can be part of the input, and you should keep them like they are. 
You should also test if the input is a string. If it is not, return "Input is not a string". """

def decode(string):
    if not (isinstance(string, str)):
        return "Input is not a string"
    res = ''
    for x in string:
        if x.isupper():
            res += chr(ord('Z') - (ord(x) - ord('A')))
        elif x.islower():
            res += chr(ord('z') - (ord(x) - ord('a')))
        else:
            res += x
    return res


q = decode("yvvi")  # "beer"
q
q = decode("Blf zoivzwb szw 10 yvvih")  # "You already had 10 beers"
q
q = decode("Ovg'h hdrn rm gsv ulfmgzrm!")  # "Let's swim in the fountain!"
q
q = decode("Tl slnv, blf'iv wifmp")  # "Go home, you're drunk"
q
q = decode(123)  # Invalid
q
