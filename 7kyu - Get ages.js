function getAges(sum, difference) {
    if (sum < 0 || difference < 0 || sum < difference) {
        return null
    }
    return [(sum + difference) / 2, (sum - difference) / 2]
}

// const getAges = (sum, diff) => (sum < 0 || diff < 0 || sum < diff) ? null : [(sum + diff) / 2, (sum - diff) / 2]

q = getAges(24, 4) // [14,10]
q
q = getAges(63, -14) // null
q