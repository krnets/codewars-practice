# 7kyu - Who Took The Car Key?

""" You woke up from a massive headache and can't seem to find your car key. 
You find a note with a clue that says:

    *"If you're reading this then I have left the state and am well on my way to freedom. 
    Just to make things interesting, I have also provided something for you to track me with. Let the chase begin..."*

Given an array of binary numbers, figure out and return the culprit's message to find out who took the missing car key."""


def who_took_the_car_key(message):
    return ''.join(chr(int(x, 2)) for x in message)


q = who_took_the_car_key(
    ['01000001', '01101100', '01100101', '01111000', '01100001', '01101110',
     '01100100', '01100101', '01110010']
), 'Alexander'
q
q = who_took_the_car_key(
    ['01001010', '01100101', '01110010', '01100101', '01101101', '01111001']
), 'Jeremy'
q
q = who_took_the_car_key(
    ['01000011', '01101000', '01110010', '01101001', '01110011']
), 'Chris'
q
q = who_took_the_car_key(
    ['01001010', '01100101', '01110011', '01110011', '01101001', '01100011',
     '01100001']
), 'Jessica'
q
q = who_took_the_car_key(
    ['01001010', '01100101', '01110010', '01100101', '01101101', '01111001']
), 'Jeremy'
q
