// 6kyu - Checking Groups

/* In English and programming, groups can be made using symbols such as () and {} that change meaning. 
However, these groups must be closed in the correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for correct grouping. 
For instance, the following groups are done correctly:
({})
[[]()]
[{()}]

The next are done incorrectly:
{(})
([]
[])

A correct string cannot close groups in the wrong order, open a group but fail to close it, or close a group before it is opened.
Your function will take an input string that may contain any of the symbols (), {} or [] to create groups.
It should return True if the string is empty or otherwise grouped correctly, or False if it is grouped incorrectly.

Algorithms | Data Structures | Strings */


// function groupCheck(s) {
//     while (/\(\)|\[\]|\{\}/.test(s))
//         s = s.replace(/\(\)|\[\]|\{\}/, '')
//     return s.length == 0
// }

// function groupCheck(s) {
//     let pairs = /\(\)|\[\]|\{\}/
//     while (pairs.test(s))
//         s = s.replace(pairs, '')
//     return s.length == 0
// }

function groupCheck(s) {
    let pairs = { '(': ')', '{': '}', '[': ']' }
    let stack = []
    for (let c of s) {
        if (c in pairs) {
            stack.push(c)
        } else if (pairs[stack[stack.length - 1]] == c) {
            stack.pop()
        } else {
            return false
        }
    }
    return stack.length == 0
}

q = groupCheck("()") // true "That group was matched correctly");
q
q = groupCheck("{(})") // false "That group was matched incorrectly");
q
q = groupCheck("[])") //false "That group was left open or prematurely closed");
q