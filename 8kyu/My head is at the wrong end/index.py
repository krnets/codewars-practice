# 8kyu - My head is at the wrong end!

""" You're at the zoo... all the meerkats look weird. 
Something has gone terribly wrong - someone has gone and switched their heads and tails around!

Save the animals by switching them back. 
You will be given an array which will have three values (tail, body, head). 
It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).

Same goes for all the other arrays/lists that you will get in the tests: 
you have to change the element positions with the same exact logics - simples! """


def fix_the_meerkat(arr):
    return arr[::-1]


q = fix_the_meerkat(["tail", "body", "head"])  # ["head", "body", "tail"]
q
q = fix_the_meerkat(["tails", "body", "heads"])  # ["heads", "body", "tails"]
q
q = fix_the_meerkat(["bottom", "middle", "top"])  # ["top", "middle", "bottom"]
q
q = fix_the_meerkat(["lower legs", "torso", "upper legs"])
q
#      ["upper legs", "torso", "lower legs"]
q = fix_the_meerkat(["ground", "rainbow", "sky"])
q
#      ["sky", "rainbow", "ground"]
