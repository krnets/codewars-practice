// 7kyu - How many times does it contain?

/* Your task is to return how many times a string contains a given character.

The function takes a string(inputS) as a paremeter and a char(charS) which is the character 
that you will have to find and count.

For example, if you get an input string "Hello world" and the character to find is "o", return 2. */

const stringCounter = (inputS, charS) => [...inputS].filter(v => v == charS).length

// const stringCounter = (inputS, charS) => (inputS.match(new RegExp(`[${charS}]`, 'g')) || []).length

q = stringCounter("Hello World!","o") // 2
q
q = stringCounter("Do you like Harry Potter?","?") // 1
q
q = stringCounter("abcdefg","a") // 1
q