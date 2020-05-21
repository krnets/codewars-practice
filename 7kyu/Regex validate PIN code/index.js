// 7kyu - Regex validate PIN code

// const validatePIN = pin => /^[0-9]{4}$|^[0-9]{6}$/.test(pin)
// const validatePIN = pin => /^([0-9]{4}|[0-9]{6})$/.test(pin)
const validatePIN = pin => /^\d{4}$|^\d{6}$/.test(pin)
// const validatePIN = pin => /^(\d{4}|\d{6})$/.test(pin)
// const validatePIN = pin => /^(\d{2}){2,3}$/.test(pin)

q = validatePIN("1") // false
q
q = validatePIN("12") // false
q
q = validatePIN("123") // false
q
q = validatePIN("12345") // false
q
q = validatePIN("1234567") // false
q
q = validatePIN("-1234") // false
q
q = validatePIN("1.234") // false
q
q = validatePIN("-1.234") // false
q
q = validatePIN("00000000") // false
q
q = validatePIN("a234") // false
q
q = validatePIN(".234") // false
q

q = validatePIN("1234") // true
q
q = validatePIN("0000") // true
q
q = validatePIN("1111") // true
q
q = validatePIN("123456") // true
q
q = validatePIN("098765") // true
q
q = validatePIN("000000") // true
q
q = validatePIN("123456") // true
q
q = validatePIN("090909") // true
q