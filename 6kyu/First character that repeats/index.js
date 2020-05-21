// const firstDup = s => s.split('').filter((x, _, a) => a.indexOf(x) !== a.lastIndexOf(x))[0] || null;

function firstDup(str) {
    return str.split('')
              .filter((value, _, array) => 
                  array.indexOf(value) !== array.lastIndexOf(value))[0] || undefined
}

// const firstDup = ([head, ...tail]) => tail.includes(head) ? firstDup(tail.filter(char => char == head)) : head || null

// function firstDup (s) {
//     return s[s.search(/(.).*\1/ )]
//   }

// function firstDup(s) {
//     for (var i = 0; i < s.length; ++i) {
//         if (s.indexOf(s[i], i + 1) != -1)
//             return s[i];
//     }
// }

const assertEquals = (fn, cmp) => fn == cmp

q = assertEquals(firstDup('tweet'), 't')
q
q = assertEquals(firstDup('Ode to Joy'), ' ')
q
q = assertEquals(firstDup('ode to joy'), 'o')
q
q = assertEquals(firstDup('bar'), undefined)
q
q = assertEquals(firstDup('123123'), '1')
q
q = assertEquals(firstDup('!@#$!@#$'), '!')
q