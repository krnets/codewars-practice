// 6kyu - What's in a name?

/* ..Or rather, what's a name in? For us, a particular string is where we are looking for a name.
Test whether or not the string contains all of the letters which spell a given name, in order.

A function passing two strings, searching for one (the name) within the other. 
function nameInStr(str, name){ return true || false }

nameInStr("Across the rivers", "chris") --> true
            ^      ^  ^^   ^
            c      h  ri   s

Contains all of the letters in "chris", in order.

nameInStr("Next to a lake", "chris") --> false

Contains none of the letters in "chris".

nameInStr("Under a sea", "chris") --> false
               ^   ^
               r   s

Contains only some of the letters in "chris".

nameInStr("A crew that boards the ship", "chris") --> false
             cr    h              s i
             cr                h  s i  
             c     h      r       s i
             ...

Contains all of the letters in "chris", but not in order.

nameInStr("A live son", "Allison") --> false
           ^ ^^   ^^^
           A li   son

Contains all of the correct letters in "Allison", in order, 
but not enough of all of them (missing an 'l'). */


// function nameInStr(str, name) {
//     let count = 0
//     str = str.toLowerCase()
//     name = name.toLowerCase()
//     for (let i = 0, j = 0; i < str.length; i++) {
//         if (str[i] == name[j]) {
//             count++
//             j++
//             if (count == name.length)
//                 return true
//         }
//     }
//     return false
// }

// function nameInStr(str, name) {
//     let index = 0
//     str = str.toLowerCase()
//     name = name.toLowerCase()

//     for (let char of str)
//         if (char == name[index])
//             index++

//     return index == name.length
// }

const nameInStr = (str, name) => new RegExp([...name].join('.*'), 'i').test(str)

// function nameInStr(str, name, i = 0) {
//     [...str.toLowerCase()].forEach(v => v == (name[i] || '').toLowerCase() ? i++ : null)
//     return i == name.length
// }


q = nameInStr('Across the rivers', 'chris') // true
q
q = nameInStr('Next to a lake', 'chris') // false
q
q = nameInStr('Under a sea', 'chris') // false
q
q = nameInStr('A crew that boards the ship', 'chris') // false
q
q = nameInStr('A live son', 'Allison') // false
q
q = nameInStr('aa a ora  myobylmf axrl   myiaejj r y bltiengdg brtdlj hisanoiznyxtbrcyx ail rsza ej  hagiiyii jxtn oimyanwrfximaoa', 'Brittany')
q
// true
q = nameInStr('let rf ovniafgmraz epgni  hvy eldrnenaeysr ttrch rhambhiaa yar yye   xvwaaxma mtn raonrldma   fae c ', 'Matthew')
// true
q
q = nameInStr('ob bjmocmxvsoahrd xencyefo hijm    rrjprd  i  vdoewaxcfctdsoteefrlr faaejlibt hdjetarabaqmyyticxf oyrae b a tmo', 'Jeremy')
q
// true