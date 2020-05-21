// 7kyu - Debug Sum of Digits of a Number

// function getSumOfDigits(integer) {
//     var sum = null;
//     var digits =  Math.floor(integer).toString();
//     for(var ix = 1; ix < digits.length; ix = sum + 1) {
//       sum =+ digits[ix + 1]);
//     }
//     return sum;
//   }

function getSumOfDigits(integer) {
    var sum = 0;
    var digits = Math.floor(integer).toString();
    for (var ix = 0; ix < digits.length; ix++) {
        sum += Number(digits[ix]);
    }
    return sum;
}

// const getSumOfDigits = integer => eval([...`${integer}`].join('+'))

// const getSumOfDigits = integer => [...String(integer)].reduce((sum, d) => +d + sum, 0)
// const getSumOfDigits = int => [...(int + '')].reduce((a, b) => a + +b, 0)
// const getSumOfDigits = int => [...int + ''].reduce((a, b) => a + +b, 0)
// const getSumOfDigits = n => [...n + ``].reduce((a, b) => a + +b, 0)

q = getSumOfDigits(123) // 6
q
q = getSumOfDigits(789) // 6
q
q = getSumOfDigits('a') // 6
q