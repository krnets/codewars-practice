// 5kyu - The Hashtag Generator

/* The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false */

// function generateHashtag(str) {
//     if (!str || /^\s+$/.test(str)) return false
//     let res = '#' + str.split(' ').map(v => v ? v[0].toUpperCase() + v.slice(1) : '').join('')
//     return res.length > 140 ? false : res
// }

function generateHashtag(str) {
    let res = '#' + str.split(' ').map(v => v ? v[0].toUpperCase() + v.slice(1) : '').join('')
    return res.length > 140 || /^\s*$/.test(str) ? false : res
}

q = generateHashtag("") // false, "Expected an empty string to return false"
q
q = generateHashtag(" ".repeat(200)) // false, "Still an empty string"
q
q = generateHashtag("Do We have A Hashtag") // "#DoWeHaveAHashtag", "Expected a Hashtag (#) at the beginning."
q
q = generateHashtag("Codewars") // "#Codewars", "Should handle a single word."
q
q = generateHashtag("Codewars Is Nice") // "#CodewarsIsNice", "Should remove spaces."
q
q = generateHashtag("Codewars is nice") // "#CodewarsIsNice", "Should capitalize first letters of words."
q
q = generateHashtag("code" + " ".repeat(140) + "wars") // "#CodeWars"
q
q = generateHashtag("Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat")
//  false, "Should return false if the final word is longer than 140 chars."
q
q = generateHashtag("a".repeat(139)) // "#A" + "a".repeat(138), "Should work"
q
q = generateHashtag("a".repeat(140)) // false, "Too long"
q