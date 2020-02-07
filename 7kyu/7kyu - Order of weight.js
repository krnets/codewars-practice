// 7kyu - Order of weight

/* Given an array of strings, sort the array into order of weight from light to heavy.

Weight units are grams(G), kilo-grams(KG) and tonnes(T).

Arrays will always contain correct and positive values aswell as uppercase letters. */

// function arrange(arr) {
//     let grams = arr.filter(v => /\dG/.test(v)).sort((a, b) => a.slice(0, -1) - b.slice(0, -1))
//     let kilograms = arr.filter(v => /\dKG/.test(v)).sort((a, b) => a.slice(0, -2) - b.slice(0, -2))
//     let tonnes = arr.filter(v => /\dT/.test(v)).sort((a, b) => a.slice(0, -1) - b.slice(0, -1))
//     return grams.concat(kilograms).concat(tonnes)
// }

function arrange(arr) {
    [grams, kilograms, tonnes] = [Array(), Array(), Array()]
    arr.forEach(v => {
        if (v.endsWith('KG')) kilograms.push(v)
        else if (v.endsWith('G')) grams.push(v)
        else tonnes.push(v) })
    grams.sort((a, b) => a.slice(0, -1) - b.slice(0, -1))
    tonnes.sort((a, b) => a.slice(0, -1) - b.slice(0, -1))
    kilograms.sort((a, b) => a.slice(0, -2) - b.slice(0, -2))
    return [...grams, ...kilograms, ...tonnes]
}


q = arrange(["200G", "300G", "150G", "100KG"]) // ["150G","200G","300G","100KG"]
q
q = arrange(["400G", "100T", "150KG", "100G"]) // ["100G","400G","150KG","100T"]
q
q = arrange(["4T", "300G", "450G", "900KG"]) // ["300G","450G","900KG","4T"]
q
q = arrange(["400T", "100T", "1T", "100G"]) // ["100G","1T","100T","400T"]
q
q = arrange(["1G", "2KG", "3T", "100KG"]) // ["1G","2KG","100KG","3T"]
q
q = arrange(["100KG", "100G", "150T", "150KG"]) // ["100G","100KG","150KG","150T"]
q