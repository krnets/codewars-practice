// 6kyu - Convert it, quickly!

/* #Input: string containing a single positive valid hex number without # symbol. Ex: 'FF'.
#Output: converted decimal number, 255

#Restriction: code length <= 26 characters
#Trivia: you have time to type only 26 characters before the daily angry zombie mob will break into your house. */

// weirdHexToDec=x=>eval(`+0x${x}`)+1
// weirdHexToDec=x=>parseInt(x,16)+1
weirdHexToDec=x=>+('0x'+x)
// weirdHexToDec=x=>'0x'+x-0
// weirdHexToDec=x=>+`0x${x}`
// weirdHexToDec=x=>x

q = weirdHexToDec('FF') //  255
q