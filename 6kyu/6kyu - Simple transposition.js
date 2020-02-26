// 6kyu - Simple transposition

/* Simple transposition is a basic and simple cryptography technique. 

We make 2 rows and put first a letter in the Row 1, 
the second in the Row 2, 
third in Row 1 and so on until the end. 

Then we put the text from Row 2 next to the Row 1 text and thats it.

Complete the function that recieves a string and encrypt it with this simple transposition.

For example if the text to encrypt is: "Simple text", the 2 rows will be:
Row 1 	S 	m 	l 		e 	t
Row 2 	i 	p 	e 	t 	x 	

So the result string will be: `"Sml etipetx"` */

// function simpleTransposition(text) {
//     let row1 = [];
//     let row2 = [];
//     [...text].forEach((v, i) => i % 2 == 0 ? row1.push(v) : row2.push(v))
//     return row1.concat(row2).join('')
// }

// const simpleTransposition = text => [...text].reduce((parts, char, i) => (parts[i % 2] += char, parts), ['', '']).join('')

const simpleTransposition = text => text.replace(/./g, (c, i) => i % 2 ? '' : c) + text.replace(/./g, (c, i) => i % 2 ? c : '')

q = simpleTransposition("Sample text") // "Sml etapetx"
q
q = simpleTransposition("Simple transposition") // "Sml rnpstoipetasoiin"
q
q = simpleTransposition("All that glitters is not gold") // "Alta ltesi o odl htgitr sntgl"
q
q = simpleTransposition("The better part of valor is discretion") // "Tebte ato ao sdsrtoh etrpr fvlri icein"
q
q = simpleTransposition("Conscience does make cowards of us all") // "Cncec osmk oad fu losinede aecwrso sal"
q
q = simpleTransposition("Imagination is more important than knowledge") // "Iaiaini oeipratta nwegmgnto smr motn hnkolde"
q