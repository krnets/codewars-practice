// function firstNonRepeated(str) {
//     let myArr = [...str].map((v,i) => [...v, {count: 0}])
//     let myMap = new Map(myArr)

//     for (let c of str) {
//         myMap.get(c).count++
//     }

//     for(let c of str) {
//         if (myMap.get(c).count == 1) {
//             return c
//         }
//     }

//     return null
// }

// const firstNonRepeated = s => s.split('').filter((x, _, a) => a.indexOf(x) == a.lastIndexOf(x))[0] || null;
// const firstNonRepeated = ([hd,...tl]) => tl.includes(hd) ? firstNonRepeated(tl.filter( c => c!==hd )) : hd || null ;
// function firstNonRepeated(s) {
//     let i = 0;
//     while (i < s.length) {
//         if (s.split('').filter(e => e === s[i]).length === 1) {
//             return s[i];
//         }
//         i++;
//     }
//     return null;
// }
// const firstNonRepeated = s => [...s].filter(e => s.indexOf(e) === s.lastIndexOf(e))[0] || null;

// function firstNonRepeated(s) {
//     for (let i = 0; i < s.length; i++) {
//         if (s.indexOf(s[i]) === s.lastIndexOf(s[i])) {
//             return s[i];
//         }
//     }
//     return null;
// }

function firstNonRepeated(str) {
    for (let i = 0; i < str.length; i++) {
        if (str.indexOf(str[i]) === str.lastIndexOf(str[i]))
            return str[i];
    }
    return null
}


q = firstNonRepeated("test") // 'e'
q
q = firstNonRepeated("teeter") // 'r'
q
q = firstNonRepeated("1122321235121222") // '5'
q
q = firstNonRepeated("rend") // 'r'
q