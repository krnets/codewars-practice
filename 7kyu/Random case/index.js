// 7kyu - Random case

/* Write a function that will randomly upper and lower characters in a string - randomCase()

Note: this function will work within the basic ASCII character set to make this kata easier
so no need to make the function multibyte safe. */

// const randomCase = (x) => [...x].map(v => Math.random() < 0.5 ? v.toUpperCase() : v.toLowerCase()).join('')
const randomCase = (x) => x.replace(/\w/g, c => Math.random() < 0.5 ? c.toUpperCase() : c.toLowerCase())

q = randomCase("Lorem ipsum dolor sit amet, consectetur adipiscing elit") // "lOReM ipSum DOloR SiT AmeT, cOnsEcTEtuR aDiPiSciNG eLIt"
q
q = randomCase("Donec eleifend cursus lobortis") // "DONeC ElEifEnD CuRsuS LoBoRTIs"
q