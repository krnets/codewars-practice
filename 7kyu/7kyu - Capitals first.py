# 7kyu - Capitals first!

""" Create a function that takes an input String and returns a String, 
where all the uppercase words of the input String are in front and all the lowercase words at the end. 
The order of the uppercase and lowercase words should be the order in which they occur.

If a word starts with a number or special character, skip the word and leave it out of the result.

Input String will not be empty.

"hey You, Sort me Already!"  ->  "You, Sort Already! hey me" """


def capitals_first(text):
    arr = [x for x in text.split() if x[0].isalpha()]
    return ' '.join(sorted(arr, key=lambda x: x[0].islower()))


q = capitals_first("sense Does to That Make you?")
q
#      "Does That Make sense to you?"
q = capitals_first("hey You, Sort me Already!")
q
#      "You, Sort Already! hey me"
q = capitals_first('You Me 123 baby and')
q
#       'You Me baby and'
q = capitals_first('Life Sometimes !Hard gets pretty')
q
#      'Life Sometimes gets pretty'
