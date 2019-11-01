const rotateToMax = n => Number([...String(n)].sort((a, b) => b - a).reduce((a, b) => a.concat(b)))
// const rotateToMax = n => Number([...String(n)].sort((a, b) => b - a).join``)

q = rotateToMax(123) // 321
q
q = rotateToMax(786) // 876
q
q = rotateToMax('001') // 100
q
q = rotateToMax(999) // 999
q
q = rotateToMax(10543) // 54310
q