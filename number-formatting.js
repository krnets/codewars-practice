// function numberFormat(number) {
//     let sign = Math.sign(number) == -1 ? '-' : ''
//     let newArray = []
//     let newString = ''
//     let a = [...String(number).replace(/\D/g, '')]

//     for (let i = a.length; i > 0; i = i - 3)
//         newArray.push(a.splice(-3).join(''))

//     for (let i = newArray.length; i > 0; i--)
//         newString += newArray[i - 1] + ','

//     return sign + newString.slice(0, newString.length - 1)
// }

// function numberFormat (number) {
//     return number.toLocaleString()
// }

// const numberFormat = n => new Intl.NumberFormat('en-US' ).format(n)

const numberFormat = n => n.toLocaleString()


q = numberFormat(100000) // '100,000'
q
q = numberFormat(5678545) // '5,678,545'
q
q = numberFormat(-5678545) // '5,678,545'
q