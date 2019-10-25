// const specialNumber = n => String(n).split('').every(n => n >= 0 && n < 6) ? 'Special!!' : 'NOT!!'
const specialNumber = n => /[6-9]/.test(n) ? "NOT!!" : "Special!!"

q = specialNumber(2) // "Special!!"
q
q = specialNumber(3) // "Special!!"
q
q = specialNumber(6) // "NOT!!"
q
q = specialNumber(9) //,"NOT!!"
q
q = specialNumber(11) //,"Special!!"
q
q = specialNumber(55) //,"Special!!"
q
q = specialNumber(26) //,"NOT!!"
q
q = specialNumber(92) //,"NOT!!"
q
q = specialNumber(25432) //,"Special!!"
q
q = specialNumber(2783) //,"NOT!!"
q