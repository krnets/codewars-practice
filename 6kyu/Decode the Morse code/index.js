// 6kyu - Decode the Morse code

const MORSE_CODE = {
    '...---...': 'SOS',
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '-----': '0',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '.-.-.-': '.',
    '-.-.--': '!',
}

// const decodeMorse = morseCode => morseCode.split(' ').map(v => MORSE_CODE[v] || ' ').join ``.replace(/\s+/g, ' ').trim()
// const decodeMorse = morseCode => morseCode.trim().replace(/\s?[.-]+\s?/g, match => MORSE_CODE[match.trim()])
// const decodeMorse = morseCode => morseCode.trim().replace(/\s?[.-]+\s?/g, match => MORSE_CODE[match])
// const decodeMorse = morseCode => morseCode.trim().replace(/([\.-]+) ? ?/g, (_, c) => MORSE_CODE[c])

const decodeMorse = morseCode => morseCode.trim().split(/  | /).map(v => MORSE_CODE[v] || ' ').join ``


q = decodeMorse('.... . -.--   .--- ..- -.. .') // 'HEY JUDE'
q

// const morse = {
//     'SOS': '...---...',
//     'A': '.-',
//     'B': '-...',
//     'C': '-.-.',
//     'D': '-..',
//     'E': '.',
//     'F': '..-.',
//     'G': '--.',
//     'H': '....',
//     'I': '..',
//     'J': '.---',
//     'K': '-.-',
//     'L': '.-..',
//     'M': '--',
//     'N': '-.',
//     'O': '---',
//     'P': '.--.',
//     'Q': '--.-',
//     'R': '.-.',
//     'S': '...',
//     'T': '-',
//     'U': '..-',
//     'V': '...-',
//     'W': '.--',
//     'X': '-..-',
//     'Y': '-.--',
//     'Z': '--..',
//     '0': '-----',
//     '1': '.----',
//     '2': '..---',
//     '3': '...--',
//     '4': '....-',
//     '5': '.....',
//     '6': '-....',
//     '7': '--...',
//     '8': '---..',
//     '9': '----.',
//     '.': '.-.-.-',
//     '!': '-.-.--',
// }

// function decodeMorse(morseCode) {
//     let keys = Object.keys(morse)
//     let vals = Object.values(morse)
//     return morseCode.split(' ').map(v => keys[vals.indexOf(v)] || ' ').join ``.replace(/\s+/g, ' ').trim()
// }