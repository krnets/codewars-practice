function password(str) {
    return /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.{8,})/.test(str)
    // return /(?=.*\d)(?=.*[a-zA-Z])(?=.{8})/g.test(str)
    // return str.length >= 8 && /[a-z]/.test(str) && /[A-Z]/.test(str) && /\d/.test(str)
    // return str.length >= 8 && /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])/.test(str)
}
// /^[a-zA-Z0-9]*$/
    return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{8,}/.test(str)

q = password("Abcd1234") // true
q
q = password("Abcd123") // false
q
q = password("abcd1234") // false
q
q = password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890") // true
q
q = password("ABCD1234") // false
q
q = password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,") // true
q
q = password("!@#$%^&*()-_+={}[]|\:;?/>.<,") // false
q