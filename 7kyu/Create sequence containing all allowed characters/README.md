### Create sequence containing all allowed characters

Define createSequence(regex) function that returns a string of all characters (in ASCII order) matching specified regular expression one-character criterion.

Examples
```
let digits = /[0-9]/;
// createSequence(digits) === '0123456789'

let hexadecimal = /[0-9A-F]/;
// createSequence(hexadecimal) === '0123456789ABCDEF'
