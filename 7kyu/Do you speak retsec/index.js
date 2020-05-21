// 7kyu - Do you speak retsec?

/* You and your friends want to play undercover agents. In order to exchange your secret messages, you've come up with 
the following system: you take the word, cut it in half, and place the first half behind the latter. 
If the word has an uneven number of characters, you leave the middle at its previous place.

That way, you'll be able to exchange your messages in private.
You're given a single word. Your task is to swap the halves. If the word has an uneven length, 
leave the character in the middle at that position and swap the chunks around it.

reverseByCenter("secret")  == "retsec" // no center character
reverseByCenter("agent")   == "nteag"  // center character is "e" */

function reverseByCenter(s) {
    let left = s.slice(0, s.length / 2)
    let right = s.length % 2 == 0 ? s.slice(s.length / 2) : s.slice(s.length / 2 + 1)
    let middle = s.length % 2 == 1 ? s.substr(s.length / 2, 1) : ''
    return [right, middle, left].join('')
}

q = reverseByCenter("secret") // "retsec"
q
q = reverseByCenter("agent") // "nteag"
q
q = reverseByCenter("raw") // "war"
q
q = reverseByCenter("onion") // "onion"
q