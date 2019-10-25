// const fixTheMeerkat = (arr) => arr.reverse() 
const fixTheMeerkat = ([tail, body, head]) => [head, body, tail]


q = fixTheMeerkat(["tail", "body", "head"]) // ["head", "body", "tail"]
q
q = fixTheMeerkat(["tails", "body", "heads"]) // ["heads", "body", "tails"]
q
q = fixTheMeerkat(["bottom", "middle", "top"]) // ["top", "middle", "bottom"]
q
q = fixTheMeerkat(["lower legs", "torso", "upper legs"]) // ["upper legs", "torso", "lower legs"]
q
q = fixTheMeerkat(["ground", "rainbow", "sky"]) // ["sky", "rainbow", "ground"]
q