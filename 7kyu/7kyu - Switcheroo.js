// 7kyu - Switcheroo

/* Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). 
Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb' */

const switcheroo = x => x.replace(/[ab]/g, m => (m == 'a' ? 'b' : 'a'))

q = switcheroo('abc') // 'bac'
q
q = switcheroo('aaabcccbaaa') // 'bbbacccabbb'
q
q = switcheroo('ccccc') // 'ccccc'
q
