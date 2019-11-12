// 7kyu - Celebrity Baby Names

// function validName(array) {
//     for (var count = 0, i = 0; i < array.length - 1; i++)
//         if (array[i].slice(-1).toUpperCase() == array[i + 1].slice(0, 1))
//             count++

//     return (array.length == 1) ? "Congratulations, you can choose any name you like!" :
//         (count == array.length - 1) ? 'Congratulations, your baby names are compatible!' :
//         (!array || array.length == 0) ? 'You must test at least one name.' :
//         'Back to the drawing board, your baby names are not compatible.'
// }

function validName(array) {
    if (!array || array.length == 0) return 'You must test at least one name.'

    for (var count = 0, i = 0; i < array.length - 1; i++)
        if (array[i].slice(-1).toUpperCase() == array[i + 1].slice(0, 1))
            count++

    return (array.length == 1) ? 'Congratulations, you can choose any name you like!' :
        (count == array.length - 1) ? 'Congratulations, your baby names are compatible!' :
        'Back to the drawing board, your baby names are not compatible.'
}

// const validName = xs => xs.length ? xs.length > 1 ? xs.slice(0, -1).every((x, i) => x[x.length - 1].toUpperCase() == xs[i + 1][0]) ?
//     "Congratulations, your baby names are compatible!" : "Back to the drawing board, your baby names are not compatible." :
//     "Congratulations, you can choose any name you like!" : "You must test at least one name."

// const validName = a => !a.length ? 'You must test at least one name.' : 
//                         a.length == 1 ? 'Congratulations, you can choose any name you like!' : 
//                         a.map(s => s.toLowerCase()).some((s, i, a) => i && s[0] != a[i - 1].slice(-1)) ? 
//                         'Back to the drawing board, your baby names are not compatible.' : 
//                         'Congratulations, your baby names are compatible!';


q = validName(["Cruz", "Zuma"])
// "Congratulations, your baby names are compatible!"
q
q = validName(["Buddy Bear", "Romeo", "Olive"])
// "Congratulations, your baby names are compatible!"
q
q = validName(["Peaches", "Saint", "Theodora", "Ava", "Apple", "Egypt", "Tallulah", "Harlow", "Willow", "Weston", "Nala", "Atlas", "Silas", "Sundance", "Esmeralda", "Angel", "Lily-Rose", "Ever", "Rebel", "Lourdes"])
// "Congratulations, your baby names are compatible!"
q
q = validName(["Jaden"])
// "Congratulations, you can choose any name you like!"
q
q = validName(["George", "Charlotte"])
// "Back to the drawing board, your baby names are not compatible."
q
q = validName([])
q