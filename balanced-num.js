function balancedNum(num) {
    let numString = num.toString()
    let numLength = num.toString().length

    if (numLength <= 2) {
        return 'Balanced'
    } else if (numLength % 2 == 0) {
        let c = Math.floor(numLength / 2)
        let leftSum = numString.slice(0, c - 1)
            .split('')
            .map(x => parseInt(x))
            .reduce((a, b) => a + b, 0)
        let rightSum = numString.slice(c + 1)
            .split('')
            .map(x => parseInt(x))
            .reduce((a, b) => a + b, 0)
        return leftSum == rightSum ? 'Balanced' : 'Not Balanced'
    } else {
        let c = Math.floor(numLength / 2)
        let leftSum = numString.slice(0, c)
            .split('')
            .map(x => parseInt(x))
            .reduce((a, b) => a + b, 0)
        let rightSum = numString.slice(c + 1)
            .split('')
            .map(x => parseInt(x))
            .reduce((a, b) => a + b, 0)
        return leftSum == rightSum ? 'Balanced' : 'Not Balanced'
    }
}

q = balancedNum(7) // "Balanced")
q
q = balancedNum(959) // "Balanced")
q
q = balancedNum(13) // "Balanced")
q
q = balancedNum(432) // "Not Balanced")
q
q = balancedNum(424) // "Balanced")
q
q = balancedNum(1024) // "Not Balanced")
q
q = balancedNum(66545) // "Not Balanced")
q
q = balancedNum(295591) // "Not Balanced")
q
q = balancedNum(1230987) // "Not Balanced")
q
q = balancedNum(56239814) // "Balanced")
q