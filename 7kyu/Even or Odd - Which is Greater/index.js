// 7kyu - Even or Odd - Which is Greater?

/* Given a string of numbers confirm whether the total of all the individual even numbers 
are greater than the total of all the indiviudal odd numbers. Always a string of numbers will be given.

If the sum of even numbers is greater than the odd numbers return:
'Even is greater than Odd'

If the sum of odd numbers is greater than the sum of even numbers return:
'Odd is greater than Even'

If the total of both even and odd numbers are identical return:
'Even and Odd are the same' */

function evenOrOdd(str) {
    let oddSum  = [...str].filter(v => v % 2 != 0).reduce((a, b) => a + Number(b), 0)
    let evenSum = [...str].filter(v => v % 2 == 0).reduce((a, b) => a + Number(b), 0)

    return oddSum < evenSum ? 'Even is greater than Odd' :
           oddSum > evenSum ? 'Odd is greater than Even' : 
           'Even and Odd are the same'
}

q = evenOrOdd('12') // 'Even is greater than Odd'
q
q = evenOrOdd('123') // 'Odd is greater than Even'
q
q = evenOrOdd('112') // 'Even and Odd are the same'
q