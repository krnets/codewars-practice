""" 6kyu - Resistor Color Codes, Part 2

Resistors are electrical components marked with colorful stripes/bands to indicate both their resistance value in ohms 
and how tight a tolerance that value has. If you did my Resistor Color Codes kata, you wrote a function which took 
a string containing a resistor's band colors, and returned a string identifying the resistor's ohms and tolerance values.

Well, now you need that in reverse: The previous owner of your "Beyond-Ultimate Raspberry Pi Starter Kit" 
(as featured in my Fizz Buzz Cuckoo Clock kata) had emptied all the tiny labeled zip-lock bags of components into the box, 
so that for each resistor you need for a project, instead of looking for text on a label, you need to find one with 
the sequence of band colors that matches the ohms value you need.

The resistor color codes

You can see this Wikipedia page for a colorful chart, but the basic resistor color codes are:

0: black, 1: brown, 2: red, 3: orange, 4: yellow, 5: green, 6: blue, 7: violet, 8: gray, 9: white

All resistors have at least three bands, with the first and second bands indicating the first two digits of the ohms value, 
and the third indicating the power of ten to multiply them by, for example a resistor with a value of 47 ohms, 
which equals 47 * 10^0 ohms, would have the three bands "yellow violet black".

Most resistors also have a fourth band indicating tolerance -- in an electronics kit like yours, 
the tolerance will always be 5%, which is indicated by a gold band. 
So in your kit, the 47-ohm resistor in the above paragraph would have the four bands "yellow violet black gold".

Your function will receive a string containing the ohms value you need, followed by a space and the word "ohms" 
(to avoid Codewars unicode headaches I'm just using the word instead of the ohms unicode symbol). 
The way an ohms value is formatted depends on the magnitude of the value:

    For resistors less than 1000 ohms, the ohms value is just formatted as the plain number. 
    For example, with the 47-ohm resistor above, your function would receive the string "47 ohms", 
    and return the string `"yellow violet black gold".

    For resistors greater than or equal to 1000 ohms, but less than 1000000 ohms, the ohms value is divided by 1000, 
    and has a lower-case "k" after it. For example, if your function received the string "4.7k ohms", 
    it would need to return the string "yellow violet red gold".

    For resistors of 1000000 ohms or greater, the ohms value is divided by 1000000, and has an upper-case "M" after it. 
    For example, if your function received the string "1M ohms", it would need to return the string "brown black green gold".

Test case resistor values will all be between 10 ohms and 990M ohms.
More examples, featuring some common resistor values from your kit

"10 ohms"        "brown black black gold"
"100 ohms"       "brown black brown gold"
"220 ohms"       "red red brown gold"
"330 ohms"       "orange orange brown gold"
"470 ohms"       "yellow violet brown gold"
"680 ohms"       "blue gray brown gold"
"1k ohms"        "brown black red gold"
"10k ohms"       "brown black orange gold"
"22k ohms"       "red red orange gold"
"47k ohms"       "yellow violet orange gold"
"100k ohms"      "brown black yellow gold"
"330k ohms"      "orange orange yellow gold"
"2M ohms"        "red black green gold" """

# RES_COLORS = {str(v): k for k, v in dict(black=0, brown=1, red=2, orange=3, yellow=4, green=5, blue=6, violet=7, gray=8, white=9).items()}

# def encode_resistor_colors(ohms_string):
#     ohms = ohms_string.split()[0]
#     ohms = str(int(float(ohms[:-1]) * 1e3) if 'k' in ohms else int(float(ohms[:-1]) * 1e6) if 'M' in ohms else ohms)
#     return ' '.join([RES_COLORS.get(ohms[0]), RES_COLORS.get(ohms[1]), RES_COLORS.get(str(len(ohms)-2)), 'gold'])

RES_COLORS = 'black brown red orange yellow green blue violet gray white'.split()

# def encode_resistor_colors(ohms_string):
#     ohms = ohms_string.split()[0]
#     ohms = str(int(float(ohms[:-1]) * 1e3) if 'k' in ohms else int(float(ohms[:-1]) * 1e6) if 'M' in ohms else ohms)
#     return ' '.join([RES_COLORS[int(ohms[0])], RES_COLORS[int(ohms[1])], RES_COLORS[len(ohms)-2], 'gold'])

# def encode_resistor_colors(ohms_string):
#     ohms = str(int(eval(ohms_string.replace('k', '*1e3').replace('M', '*1e6').split()[0])))
#     return '%s %s %s gold' % (RES_COLORS[int(ohms[0])], RES_COLORS[int(ohms[1])], RES_COLORS[len(ohms)-2])

def encode_resistor_colors(ohms_string):
    t, u, *p = str(int(eval(ohms_string.replace('k', '*1e3').replace('M', '*1e6').split()[0])))
    return '%s %s %s gold' % (RES_COLORS[int(t)], RES_COLORS[int(u)], RES_COLORS[len(p)])


q = encode_resistor_colors("10 ohms"), "brown black black gold"
q
q = encode_resistor_colors("47 ohms"), "yellow violet black gold"
q
q = encode_resistor_colors("100 ohms"), "brown black brown gold"
q
q = encode_resistor_colors("220 ohms"), "red red brown gold"
q
q = encode_resistor_colors("330 ohms"), "orange orange brown gold"
q
q = encode_resistor_colors("470 ohms"), "yellow violet brown gold"
q
q = encode_resistor_colors("680 ohms"), "blue gray brown gold"
q
q = encode_resistor_colors("1k ohms"), "brown black red gold"
q
q = encode_resistor_colors("4.7k ohms"), "yellow violet red gold"
q
q = encode_resistor_colors("10k ohms"), "brown black orange gold"
q
q = encode_resistor_colors("22k ohms"), "red red orange gold"
q
q = encode_resistor_colors("47k ohms"), "yellow violet orange gold"
q
q = encode_resistor_colors("100k ohms"), "brown black yellow gold"
q
q = encode_resistor_colors("330k ohms"), "orange orange yellow gold"
q
q = encode_resistor_colors("1M ohms"), "brown black green gold"
q
q = encode_resistor_colors("2M ohms"), "red black green gold"
q
