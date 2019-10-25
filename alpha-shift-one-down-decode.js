// function oneDown(str) {
//     var alph = "zABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

//     return typeof str === "string" ?
//         str.replace(/\w/g, v => alph.charAt(alph.lastIndexOf(v) - 1)) :
//         "Input is not a string";
// }

// function oneDown(str) {
//     let dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';

//     return typeof str === 'string' ?
//         str.replace(/[a-z]/gi, c => dict[(dict.indexOf(c) + 51) % 52]) :
//         'Input is not a string';

// }

// const key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
// const oneDown = s => typeof s === 'string' ? s.replace(/\w/g, c => key[key.indexOf(c) - 1] || 'z') : 'Input is not a string';


function oneDown(str) {
    let key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';

    return typeof str === 'string' ?
        str.replace(/\w/g, c => key[key.indexOf(c) - 1] || 'z') :
        'Input is not a string';
}

q = oneDown(" ") // "The trick to this kata is simple"
q
q = oneDown("A")
q
q = oneDown("Ifmmp") // "Hello"
q
q = oneDown("Uif usjdl up uijt lbub jt tjnqmf") // "The trick to this kata is simple"
q
q = oneDown(45) // "Input is not a string"
q