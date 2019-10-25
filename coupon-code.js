function checkCoupon(enteredCode, correctCode, currentDate, expirationDate) {
    return enteredCode == correctCode &&
        Date.parse(currentDate) <= Date.parse(expirationDate)
}

q = checkCoupon('123', '123', 'September 5, 2014', 'October 1, 2014')
q
q = checkCoupon('123', '123', 'September 5, 2014', 'August 5, 2014') // false);
q

const assertEquals = (fn, cmp) => fn == cmp

q = assertEquals(checkCoupon('123','123','September 5, 2014','October 1, 2014'), true);
q
q = assertEquals(checkCoupon('123a','123','September 5, 2014','October 1, 2014'), false);
q