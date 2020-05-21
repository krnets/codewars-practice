// 5kyu - Word Finder

/* In this kata you have to extend the dictionary with a method, that returns a list of words matching a pattern. 
This pattern may contain letters (lowercase) and placeholders ("?"). 
A placeholder stands for exactly one arbitrary letter.

Example:

var fruits = new Dictionary(['banana', 'apple', 'papaya', 'cherry']);
fruits.getMatchingWords('lemon');     // must return []
fruits.getMatchingWords('cherr??');   // must return []
fruits.getMatchingWords('?a?a?a');    // must return ['banana', 'papaya']
fruits.getMatchingWords('??????');    // must return ['banana', 'papaya', 'cherry']

Additional Notes:

    the words and patterns are all lowercase
    the order of the returned words doesn't matter */

function Dictionary(words) {
    this.words = words;
}

// Dictionary.prototype.getMatchingWords = function (pattern) {
//     let re = new RegExp(pattern.replace(/\?/g, '.'))
//     return this.words.filter(v => re.test(v) && v.length == pattern.length)
// }

Dictionary.prototype.getMatchingWords = function (pattern) {
    let re = new RegExp(`^${pattern.replace(/\?/g, '.')}$`)
    return this.words.filter(v => re.test(v))
}


var fruits = new Dictionary(['banana', 'apple', 'papaya', 'cherry', 'blackberry', 'raspberry', 'strawberry']);
q = fruits.getMatchingWords('lemon'); // must return []
q
q = fruits.getMatchingWords('cherr??'); // must return []
q
q = fruits.getMatchingWords('?a?a?a'); // must return ['banana', 'papaya']
q
q = fruits.getMatchingWords('??????'); // must return ['banana', 'papaya', 'cherry']
q
q = fruits.getMatchingWords('?????berry');
//  '[\'blackberry\', \'strawberry\']', instead got: '[\'blackberry\', \'raspberry\', \'strawberry\']'
q