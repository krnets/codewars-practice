// 6kyu - replaceAll(input, find, replace)

// const replaceAll = (input, find, replace) => find.length ? input.split(find).join(replace) :
//     input.length ? [...input].map(v => replace + v + replace).join ``.replace(/--/g, '-') :
//     replace

// const replaceAll = (input, find, replace) => {
//     if (find == '') input = ' ' + input + ' ';
//     return input.split(find).join(replace).trim()
// }

// function replaceAll(input, find, rep) {
//     let arr = input.split(find);
//     if (find.length == 0) {
//         arr.unshift('');
//         arr.push('');
//     }
//     return arr.join(rep)
// }

// function replaceAll(input, find, replace) {
//     if (!(/\W/.test(find)))
//         return input.replace(new RegExp(find, 'g'), replace)
//     while (input.indexOf(find) >= 0)
//         input = input.replace(find, replace)
//     return input
// }

// const replaceAll = (input, find, replace) => find[0] == '\\' ? input.replace(find, replace) : input.replace(new RegExp(find, 'g'), replace)
// const replaceAll = (input, find, replace) => input.replace(new RegExp(find.replace(/\W/g, '\\$&'), 'g'), replace)
const replaceAll = (input, find, replace) => input.replace(RegExp(find.replace(/\W/g, '\\$&'), 'g'), replace)

q = replaceAll("string-string", "ing", "!") // str!-str!
q
q = replaceAll("", "", "-") // -
q
q = replaceAll("1", "", "-") // -1-
q
q = replaceAll("123", "", "-") // -1-2-3-
q