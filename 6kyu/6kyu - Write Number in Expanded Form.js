// 6kyu - Write Number in Expanded Form

/* Given a number, return it as a string in Expanded Form. For example:

expandedForm(12); // Should return '10 + 2'
expandedForm(42); // Should return '40 + 2'
expandedForm(70304); // Should return '70000 + 300 + 4'

All numbers will be whole numbers greater than 0. */

// const expandedForm = num => [...num + ''].reverse().map((v, i) => v * Math.pow(10, i)).filter(v => v).reverse().join(' + ')
// const expandedForm = num => [...num + ''].map((v, i, a) => v + '0'.repeat(a.length - i - 1)).filter(Number).join(' + ')

// const expandedForm = num => [...num + ''].reverse()
//     .reduceRight((res, n, i) => n > 0 ? res.concat(n * Math.pow(10, i)) : res, [])
//     .join(' + ')

const expandedForm = num => [...num + ''].reverse().filter(Number)
    .reduceRight((res, n, i) => res.concat(n * Math.pow(10, i)), [])
    .join(' + ')


q = expandedForm(12) // '10 + 2'
q
q = expandedForm(42) // '40 + 2'
q
q = expandedForm(70304) // '70000 + 300 + 4'
q