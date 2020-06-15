""" 7kyu - Mobile operator detector

When a warrior wants to talk with another one about peace or war he uses a smartphone. 
In one distinct country warriors who spent all time in training kata not always have enough money. 
So if they call some number they want to know which operator serves this number.

Write a function which accepts number and return name of operator or string "no info", 
if operator can't be defined. number always looks like 8yyyxxxxxxx, where yyy corresponds to operator.

Here is short list of operators:

    039 xxx xx xx - Golden Telecom
    050 xxx xx xx - MTS
    063 xxx xx xx - Life:)
    066 xxx xx xx - MTS
    067 xxx xx xx - Kyivstar
    068 xxx xx xx - Beeline
    093 xxx xx xx - Life:)
    095 xxx xx xx - MTS
    096 xxx xx xx - Kyivstar
    097 xxx xx xx - Kyivstar
    098 xxx xx xx - Kyivstar
    099 xxx xx xx - MTS Test [Just return "MTS"] """


MOB_OP = {'039': 'Golden Telecom', '050': 'MTS', '063': 'Life:)', '066': 'MTS', '067': 'Kyivstar', '068': 'Beeline',
          '093': 'Life:)', '095': 'MTS', '096': 'Kyivstar', '097': 'Kyivstar', '098': 'Kyivstar', '099': 'MTS'}


def detect_operator(num):
    return MOB_OP.get(num[1:4], 'no info')


q = detect_operator("80661111841"), "MTS"
q
q = detect_operator("80671991111"), "Kyivstar"
q
q = detect_operator("80631551111"), "Life:)"
q
q = detect_operator("80931551111"), "Life:)"
q
q = detect_operator("80111551111"), "no info"
q
