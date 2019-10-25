function disariumNumber(n) {
    let a = n.toString()
    let sum = 0
    for (let i = 0; i < a.length; i++) 
        sum += Math.pow(a[i], i+1)
    return  sum == n ? 'Disarium !!' : 'Not !!'
}

q = disariumNumber(89) // "Disarium !!"
q
q = disariumNumber(564) // "Not !!"
q
q = disariumNumber(1024) // "Not !!"
q
q = disariumNumber(135) // "Disarium !!"
q
q = disariumNumber(136586) // "Not !!"
q