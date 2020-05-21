// 7kyu - Valid HK Phone Number

/* In Hong Kong, a valid phone number has the format xxxx xxxx where x is a decimal digit (0-9). For example:

"1234 5678" // is valid
"2359 1478" // is valid
"85748475" // invalid, as there are no spaces separating the first 4 and last 4 digits
"3857  4756" // invalid; there should be exactly 1 whitespace separating the first 4 and last 4 digits respectively
"sklfjsdklfjsf" // clearly invalid
"     1234 5678   " // is NOT a valid phone number but CONTAINS a valid phone number
"skldfjs287389274329dklfj84239029043820942904823480924293042904820482409209438dslfdjs9345 8234sdklfjsdkfjskl28394723987jsfss2343242kldjf23423423SDLKFJSLKsdklf" // also contains a valid HK phone number (9345 8234)

Define two functions, isValidHKPhoneNumber and hasValidHKPhoneNumber, that returns whether a given string is a valid HK phone number and contains a valid HK phone number respectively (i.e. true/false values).

Fundamentals | Regular Expressions | Declarative Programming | Advanced Language Features | Strings */

const isValidHKPhoneNumber = str => /^\d{4} \d{4}$/.test(str)
const hasValidHKPhoneNumber = str => /\d{4} \d{4}/.test(str)


q = isValidHKPhoneNumber("1234 5678") // true
q
q = isValidHKPhoneNumber("2359 1478") // true
q
q = isValidHKPhoneNumber("85748475") // false
q
q = isValidHKPhoneNumber("3857  4756") // false
q
q = isValidHKPhoneNumber("sklfjsdklfjsf") // false
q
q = isValidHKPhoneNumber("     1234 5678   ") // false
q

q = hasValidHKPhoneNumber("Hello, my phone number is 1234 5678") // true
q
q = hasValidHKPhoneNumber("I wonder if 2359 1478 is a valid phone number?") // true
q
q = hasValidHKPhoneNumber("85748475 is definitely invalid") // false
q
q = hasValidHKPhoneNumber("'3857  4756' is so close to a valid phone number!") // false
q
q = hasValidHKPhoneNumber("sklfjsdklfjsf") // false
q
q = hasValidHKPhoneNumber("     1234 5678   ") // true
q