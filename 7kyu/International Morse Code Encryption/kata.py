CHAR_TO_MORSE = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "h": "....",
    "o": "---",
    "u": "..-",
    "b": "-...",
    "i": "..",
    "p": ".--.",
    "v": "...-",
    "c": "-.-.",
    "j": ".---",
    "q": "--.-",
    "w": ".--",
    "d": "-..",
    "k": "-.-",
    "r": ".-.",
    "x": "-..-",
    "e": ".",
    "l": ".-..",
    "s": "...",
    "y": "-.--",
    "f": "..-.",
    "m": "--",
    "t": "-",
    "z": "--..",
    "g": "--.",
    "n": "-.",
    "A": ".-",
    "H": "....",
    "O": "---",
    "U": "..-",
    "B": "-...",
    "I": "..",
    "P": ".--.",
    "V": "...-",
    "C": "-.-.",
    "J": ".---",
    "Q": "--.-",
    "W": ".--",
    "D": "-..",
    "K": "-.-",
    "R": ".-.",
    "X": "-..-",
    "E": ".",
    "L": ".-..",
    "S": "...",
    "Y": "-.--",
    "F": "..-.",
    "M": "--",
    "T": "-",
    "Z": "--..",
    "G": "--.",
    "N": "-.",
}


def encryption(string):
    return " ".join(CHAR_TO_MORSE.get(c, " ") for c in string)
