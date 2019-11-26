// 7kyu - NATO Phonetic Alphabet

/* Create the function nato that takes a word and returns a string spells the word using the NATO phonetic alphabet.
There should be a space between each word in the returned string, and the first letter of each word should be capitalized. */


var nato = (function () {
    var letters =  {
      "A": "Alpha",  "B": "Bravo",   "C": "Charlie",
      "D": "Delta",  "E": "Echo",    "F": "Foxtrot",
      "G": "Golf",   "H": "Hotel",   "I": "India",
      "J": "Juliett","K": "Kilo",    "L": "Lima",
      "M": "Mike",   "N": "November","O": "Oscar",
      "P": "Papa",   "Q": "Quebec",  "R": "Romeo",
      "S": "Sierra", "T": "Tango",   "U": "Uniform",
      "V": "Victor", "W": "Whiskey", "X": "X-ray",
      "Y": "Yankee", "Z": "Zulu"
    }

    return function (word) {
        // return [...word].map(v => letters[v.toUpperCase()]).join(' ')
        return [...word.toUpperCase()].map(v => letters[v]).join(' ')
    }
})()

q = nato('hi') // --> 'Hotel India'
q
q = nato('abc') // --> 'Alpha Bravo Charlie'
q