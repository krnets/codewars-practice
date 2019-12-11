// 6kyu - String transformer

/* Given a string, return a new string that has transformed based on the input:

    Change case of every character, ie. lower case to upper case, upper case to lower case.
    Reverse the order of words from the input.

Note: You will have to handle multiple spaces, and leading/trailing spaces.

"Example Input" ==> "iNPUT eXAMPLE"

You may assume the input only contain English alphabet and spaces. */

const stringTransformer = (str) => str.replace(/./g, c => c.toUpperCase() == c ? c.toLowerCase() : c.toUpperCase()).split(' ').reverse().join(' ')

q = stringTransformer('Example string') // 'STRING eXAMPLE'
q