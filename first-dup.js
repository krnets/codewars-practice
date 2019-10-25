// function firstDup (s) {
//     return s[s.search(/(.).*\1/ )]
//   }

// function firstDup(s) {
//     let temp 
//     for (var i = 0; i < s.length; ++i) {
//         i
//         temp = s[i]
//         temp
//         if (s.lastIndexOf(s[i]) != i) return s[i];
//     }
// }

// function firstDup (s) {
//     let temp
//   for (var i = 0; i < s.length; i++) {
//       i
//     for (var j = i + 1; j < s.length; j++) {
//         j
//         temp = s[j]
//         temp
//       if (s[i] === s[j]) {
//         return s[i]
//       }
//     } 
//   }
// }

function firstDup(s) {
    for (var i = 0; i < s.length; ++i) {
        if (s.indexOf(s[i], i + 1) != -1)
            return s[i];
    }
}

const assertEquals = (fn, cmp) => fn == cmp

// q = firstDup('tweet') //, 't')
// q
// q = firstDup('challange') 
// q
// q = assertEquals(firstDup('tweet'), 't')
// q
// q = assertEquals(firstDup('Ode to Joy'), ' ')
// q
// q = assertEquals(firstDup('ode to joy'), 'o')
// q
// q = assertEquals(firstDup('bar'), undefined)
// q
// q = assertEquals(firstDup('123123'), '1')
// q
// q = assertEquals(firstDup('!@#$!@#$'), '!')
// q