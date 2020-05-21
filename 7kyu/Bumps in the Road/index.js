// 7kyu - Bumps in the Road

/* Your car is old, it breaks easily. 
The shock absorbers are gone and you think it can handle about 15 more bumps before it dies totally.

Unfortunately for you, your drive is very bumpy! Given a string showing either flat road ("_") or bumps ("n"), 
work out if you make it home safely. 15 bumps or under, return "Woohoo!", over 15 bumps return "Car Dead". */

// const bump = (x) => (x.match(/n/g) || []).length <= 15 ? 'Woohoo!' : 'Car Dead'
const bump = (x) => x.split('n').length < 17 ? 'Woohoo!' : 'Car Dead'

q = bump("n") // "Woohoo!"
q
q = bump("_nnnnnnn_n__n______nn__nn_nnn") // "Car Dead"
q
q = bump("______n___n_") // "Woohoo!"
q