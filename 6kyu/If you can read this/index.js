// 6kyu - If you can read this...

/* Translate a string to Pilot's alphabet (NATO phonetic alphabet) wiki.

** Input: ** If you can read
** Output: ** India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta

    Keep the punctuation, and remove the spaces.
    Use Xray without dash or space. */

function to_nato(words) {
    let NATO = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike', 'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango', 'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
    return [...words.replace(/\s/g, '').toUpperCase()].map(v => NATO[v.charCodeAt() - 65] || v).join(' ')
}

q = to_nato('If you can read') // "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta"
q
q = to_nato('Did not see that coming') // "Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf"
q
q = to_nato('go for it!') // "Golf Oscar Foxtrot Oscar Romeo India Tango !"
q