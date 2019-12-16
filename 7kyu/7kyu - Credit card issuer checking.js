// 7kyu - Credit card issuer checking

/* Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.

Complete the function getIssuer() that will use the values shown below to determine the card issuer for a given card number. 
If the number cannot be matched then the function should return the string Unknown.

| Card Type  | Begins With          | Number Length |
|------------|----------------------|---------------|
| AMEX       | 34 or 37             | 15            |
| Discover   | 6011                 | 16            |
| Mastercard | 51, 52, 53, 54 or 55 | 16            |
| VISA       | 4                    | 13 or 16      |

Examples

getIssuer(4111111111111111) == "VISA"
getIssuer(4111111111111) == "VISA"
getIssuer(4012888888881881) == "VISA"
getIssuer(378282246310005) == "AMEX"
getIssuer(6011111111111117) == "Discover"
getIssuer(5105105105105100) == "Mastercard"
getIssuer(5105105105105106) == "Mastercard"
getIssuer(9111111111111111) == "Unknown" */

// function getIssuer(number) {
//     let str = String(number)
//     if (/^(34|37)/.test(str) && str.length == 15) return 'AMEX'
//     if (/^6011/.test(str) && str.length == 16) return 'Discover'
//     if (/^4/.test(str) && (str.length == 13 || str.length == 16)) return 'VISA'
//     if (/^(51|52|53|54|55)/.test(str) && str.length == 16) return 'Mastercard'
//     return 'Unknown'
// }

const getIssuer = (number) => /^3[4|7]\d{13}$/.test(number) ? 'AMEX' :
    /^4(\d{12}|\d{15})$/.test(number) ? 'VISA' :
    /^5[1-5]\d{14}$/.test(number) ? 'Mastercard' :
    /^6011\d{12}$/.test(number) ? 'Discover' : 'Unknown'

q = getIssuer(4111111111111111) // 'VISA'
q
q = getIssuer(378282246310005) // 'AMEX'
q
q = getIssuer(5105105105105100) // "Mastercard"
q
q = getIssuer(9111111111111111) // 'Unknown'
q
q = getIssuer(6011111111111117) // "Discover"
q