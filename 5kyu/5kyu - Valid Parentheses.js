// 5kyu - Valid Parentheses

/* Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints
0 <= input.length <= 100

Algorithms | Validation | Utilities */

// function validParentheses(parens) {
//     let stack = []
//     for (let i = 0; i < parens.length; i++) {
//         if (parens[i] == '(') {
//             stack.push(parens[i])
//         } else {
//             cmp = stack.pop()
//             if (cmp != '(')
//                 return false
//         }
//     }
//     return stack.length == 0
// }

// function validParentheses(parens) {
//     let stack = []
//     for (let i in parens) {
//         if (parens[i] == '(')
//             stack.push(parens[i])
//         else
//         if (stack.pop() != '(') return false
//     }
//     return stack.length == 0
// }

// function validParentheses(parens) {
//     let count = 0
//     for (let i in parens) {
//         if ( parens[i] == '(' ) count++
//         if ( parens[i] == ')' ) count--
//         if ( count < 0 ) return false
//     }
//     return count == 0
// }

// function validParentheses(parens) {
//     let tokenizer = /[()]/g
//     let count = 0
//     let token = ''
//     while (token = tokenizer.exec(parens), token != null) {
//         if (token == '(') count++
//         if (token == ')') {
//             count--;
//             if (count < 0) return false
//         }
//     }
//     return count == 0
// }

// function validParentheses(parens) {
//     let indent = 0
//     for (let i = 0; i < parens.length && indent >= 0; i++)
//         indent += (parens[i] == '(') ? 1 : -1
//     return indent == 0
// }

// function validParentheses(parens) {
//     while (parens.length) {
//         let prev = parens
//         parens = parens.replace(/\(\)/g, '')
//         if (parens == prev) return false
//     }
//     return true
// }

// function validParentheses(parens) {
//     while(/\(\)/.test(parens))
//         parens = parens.replace('()', '')
//     return !parens.length
// }

// function validParentheses(parens) {
//     while (parens.indexOf('()') != -1)
//         parens = parens.replace('()', '')
//     return !parens.length
// }

function validParentheses(parens) {
    while (parens.includes('()'))
        parens = parens.replace('()', '')
    return !parens.length
}

// function validParentheses(parens) {
//     let open = 0
//     let walk = parens.split('').every(s => (open += s == '(' ? 1 : -1) >= 0)
//     return walk && open == 0
// }

// const validParentheses = str => ~str.indexOf('()') ? validParentheses(str.replace(/\(\)/g, '')) : !str


q = validParentheses("()") // true
q
q = validParentheses("())") // false
q