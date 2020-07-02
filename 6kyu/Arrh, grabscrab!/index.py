""" 6kyu - Arrh, grabscrab!

Pirates have notorious difficulty with enunciating. They tend to blur all the letters together and scream at people.

At long last, we need a way to unscramble what these pirates are saying.

Write a function that will accept a jumble of letters as well as a dictionary, and output a list of words that the pirate might have meant.

For example:

grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )

Should return ["sport", "ports"].

Return matches in the same order as in the dictionary. Return an empty array if there are no matches. """


def grabscrab(word, possible_words):
    sw = sorted(word)
    return [w for w in possible_words if sorted(w) == sw]


q = grabscrab("trisf", ["first"]), ["first"]
q
q = grabscrab("oob", ["bob", "baobab"]), []
q
q = grabscrab("ainstuomn", ["mountains", "hills", "mesa"]), ["mountains"]
q
q = grabscrab("oolp", ["donkey", "pool", "horse", "loop"]), [
    "pool", "loop"], "Should have found 'pool' and 'loop'"
q
q = grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]), [
    "sport", "ports"], "Should have found 'sport' and 'ports'"
q
q = grabscrab("ourf", ["one", "two", "three"]), []
q
