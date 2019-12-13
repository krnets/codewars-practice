// 6kyu - Generic numeric template formatter

/* Your goal is to create a function to format a number given a template;
if the number is not present, use the digits 1234567890 to fill in the spaces.

the template might consist of other numbers, special characters or the like: 
you need to replace only alphabetical characters(both lower - and uppercase);
if the given or default string representing the number is shorter than the template, just repeat it to fill all the spaces. */

// function numericFormatter(template, digits = '1234567890') {
//     let index = 0;
//     return template.split(' ').map(v => [...v].map(x => {
//         if (/[a-z]/i.test(x)) return digits[index++ % digits.length];
//         return x;
//     }).join('')).join(' ');
// }

const numericFormatter = (template, d = '1234567890', i = 0) => template.replace(/[A-z]/g, () => d[i++ % d.length])

q = numericFormatter("xxx xxxxx xx", "5465253289") // "546 52532 89"
q
q = numericFormatter("xxx xxxxx xx") // "123 45678 90"
q
q = numericFormatter("+555 aaaa bbbb", "18031978") // "+555 1803 1978"
q
q = numericFormatter("+555 aaaa bbbb") // "+555 1234 5678"
q
q = numericFormatter("xxxx yyyy zzzz") // "1234 5678 9012"
q
q = numericFormatter("+555 aAAA bBBB", "18031978") // "+555 1803 1978"
q