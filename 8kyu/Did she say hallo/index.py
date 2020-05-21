# 8kyu - Did she say hallo?

""" You received a whatsup message from an unknown number. Could it be from that girl/boy with a foreign accent you met yesterday evening?

Write a simple regex to check if the string contains the word hallo in different languages.

These are the languages of the possible people you met the night before:

    hello - english
    ciao - italian
    salut - french
    hallo - german
    hola - spanish
    ahoj - czech republic
    czesc - polish

you can assume the input is a string. 
to keep this a beginner exercise you don't need to check if the greeting is a subset of word ('Hallowen' can pass the test)
regex should be case insensitive to pass the tests """

import re

def validate_hello(greetings):
    return bool(re.findall('h[ae]llo|ciao|salut|hola|ahoj|czesc', greetings, re.I))

q = validate_hello('hello'), True
q
q = validate_hello('ciao bella!'), True
q
q = validate_hello('salut'), True
q
q = validate_hello('hallo, salut'), True
q
q = validate_hello('hombre! Hola!'), True
q
q = validate_hello('Hallo, wie geht\'s dir?'), True
q
q = validate_hello('AHOJ!'), True
q
q = validate_hello('czesc'), True
q
q = validate_hello('meh'), False
q
q = validate_hello('Ahoj'), True
q
q = validate_hello('You? PaSA? tSCHUSS QuE! bIEn! tREs dOInG: DOIng. qUE. TREs BiEn: hALlo HoW? quE SaLUt hoMbre BIen: vIsTA PaSA? PaSA? la; Tres hOW! DOINg! Are aRE hoW HaSta You')
q
q = validate_hello('La; qUe treS; ciaO, hoW YOU! VIstA Que: You Doing. la? hOmbre ARe: ahOJ PASA? YOu. QUe hoMbrE tSCHusS bieN! YOU; HoW: TSCHUsS? PasA ciao. WiE hAsta! HAStA:')
q
q = validate_hello('HasTa YoU! trES, qUe, BIen, HOmbRE Are? wIe la YOU YoU; aRE! WIE: czESC? HOmBRE CzeSc haStA Are. La paSa! Que; BIeN; czesc Bien BIen qUe czesC Hasta')
q