function checkForFactor(base, factor) {
    return (Math.floor(base % factor) ? false : true)
}



q = checkForFactor(10,2)
q

q = Math.floor(10 % 2)
q

q = checkForFactor(63,7)
q

q = Math.floor(63 % 7)
q

q = checkForFactor(2450,5)
q

q = checkForFactor(24612,3)
q

q = checkForFactor(9,2)
q

q = checkForFactor(653,7)
q

q = checkForFactor(2453,5)
q

q = checkForFactor(24619,3)
q