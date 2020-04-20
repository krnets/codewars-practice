# Beta - Morse Code (translate text to and from morse code)

""" Morse Code was a way early telecommunication method. 
It was a simple translation of alpha numeric characters to a series of short and long signals 
often described as dot and dashes (. -). This kata will have you take text and transform it to 
a series of dots and dashes, as well as taking a series of dots and dashes into text. 

Below are the characters and their associated morse code:

Please note that morse code does not have separate codes for upper and lower case. 
For this challenge you should assume all text to be in lower case.

To clarify both "(" and ")" are the same sequence in morse code "-.--.-". when translating 
back from morse code to text either will be acceptable.

Arrays/Lists/Hashes/Objects/Sequences for both "morse code -> character" and "character -> morse" 
code are preloaded and may be accessed as such:

  textToMorse["a"]
  morseToText[".-"] """


FROM_MORSE = {'.-...': '&', '--..--': ',', '....-': '4', '.....': '5', '-...': 'b', '-..-': 'x', '.-.': 'r', '.--': 'w', '..---': '2', '.-': 'a', '..': 'i', '..-.': 'f', '.': 'e', '.-..': 'l', '...': 's', '..-': 'u', '..--..': '?', '.----': '1', '-.-': 'k', '-..': 'd', '-....': '6', '-...-': '=', '---': 'o', '.--.': 'p', '.-.-.-': '.', '--': 'm', '-.': 'n', '....': 'h',
              '.----.': "'", '...-': 'v', '--...': '7', '-.-.-.': ';', '-....-': '-', '..--.-': '_', '-.--.-': ')', '-.-.--': '!', '--.': 'g', '--.-': 'q', '--..': 'z', '-..-.': '/', '.-.-.': '+', '-.-.': 'c', '---...': ':', '-.--': 'y', '-': 't', '.--.-.': '@', '...-..-': '$', '.---': 'j', '-----': '0', '----.': '9', '.-..-.': '"', '-.--.': '(', '---..': '8', '...--': '3', '/': ' '}
TO_MORSE = {v: k for k, v in FROM_MORSE.items()}


def translateToMorse(text):
    return ' '.join(TO_MORSE[c] for c in text.lower())


def translateToText(morse):
    return ''.join(FROM_MORSE[c] for c in morse.split())


# Translate To Mors
q = translateToMorse('Hello World')
q
#     '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'

# Translate To Text
q = translateToText('.... . .-.. .-.. --- / .-- --- .-. .-.. -..')
q
#     'hello world'
