// 7kyu - Split string by multiple delimiters


// function multipleSplit(string, delimiters = []) {
//     let char = delimiters[0]
//     for (let i = 0; i < delimiters.length; i++)
//         string = string.split(delimiters[i]).join(char)

//     return string.split(char).filter(v => v)
// }

// function multipleSplit(string, delimiters = []) {
//     let arr = [string]
//     for (let d of delimiters)
//         arr = arr.reduce((r, s) => r.concat(s.split(d)), [])

//     return arr.filter(Boolean)
// }

// function multipleSplit(string, delimiters = []) {
//     let regex = new RegExp('[' + delimiters.join('\\') + ']', 'g');
//     return string.split(regex).filter(function (str) {
//           return !!str;
//     })
// }

// function multipleSplit(string, delimiters = []) {
//     let regex = new RegExp('[' + delimiters.join('\\') + ']', 'g')
//     return string.split(regex).filter(Boolean)
// }

// const multipleSplit = (s, d = []) => d.reduce((x, c) => x.replace(new RegExp(`\\${c}`, 'g'), '&'), s).split`&`.filter(Boolean)
// const multipleSplit = (string, delimeters = []) => string.split(new RegExp(`[${delimeters.join('\\')}]`, 'g')).filter(Boolean)
const multipleSplit = (string, delimeters = []) => string.split(RegExp('['+delimeters.join('\\')+']', 'g')).filter(Boolean)


q = multipleSplit('Hi everybody!', [' ', '!'])
// ['Hi', 'everybody']
q
q = multipleSplit('(1+2)*6-3^9', ['+', '-', '(', ')', '^', '*'])
// ['1', '2', '6', '3', '9']
q
q = multipleSplit('Solve_this|kata-very\\quickly!', ['!', '|', '\\', '_', '-'])
// ['Solve', 'this', 'kata', 'very', 'quickly']
q