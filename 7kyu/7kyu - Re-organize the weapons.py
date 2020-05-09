# 7kyu - Re-organize the weapons!

""" The characters of Chima need your help. Their weapons got mixed up! They need you to write a program that accepts the name of a character in Chima then tells which weapon he/she owns.

For example: for the character "Laval" your program should return the solution "Laval-Shado Valious"

You must complete the following character-weapon pairs:

    Laval-Shado Valious,
    Cragger-Vengdualize,
    Lagravis-Blazeprowlor,
    Crominus-Grandorius,
    Tormak-Tygafyre,
    LiElla-Roarburn.

Return "Not a character" for invalid inputs. """

CHAR_WEAPON = {
    'Laval': 'Shado Valious',
    'Cragger': 'Vengdualize',
    'Lagravis': 'Blazeprowlor',
    'Crominus': 'Grandorius',
    'Tormak': 'Tygafyre',
    'LiElla': 'Roarburn'
}

def identify_weapon(character):
    return f'{character}-{CHAR_WEAPON[character]}' if character in CHAR_WEAPON else 'Not a character'


q = identify_weapon("Laval"), "Laval-Shado Valious"
q
q = identify_weapon("Tormak"), "Tormak-Tygafyre"
q
q = identify_weapon("G'loona"), "Not a character"
q
