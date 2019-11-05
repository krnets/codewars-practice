// 6kyu - Maximum Product of Parts

function maximumProductOfParts(number) {
    let a = String(number)
    a
    let b = [...a]
    b
    let splitThreeWay = [a.slice(0,1), a.slice(1,2), a.slice(2)]
    splitThreeWay
    let newArr = []
    let begin = []
    let middle = []
    let end = []

    for (let i = 0; i < a.length - 2; i++) {
        begin.push(a.slice(0,i))
        begin.push(a.slice(0,i+1))
        begin.push(a.slice(0,i+2))
        // begin.push(a.slice(0,i+3)
        // begin.push(a.slice(0,i+4))
        // end.push(a.slice(-(i+1)))
        // end.push(a.slice(-(i+2)))
        // end.push(a.slice(-(i+3)))
        // end.push(a.slice(-(i+4)))
        // middle.push(a.slice(1,i+1))
        // middle.push(a.slice(1, i+2))
        // middle.push(a.slice(1, i+3))
        // middle.push(a.slice(1, i+4))
    }

    // let c = newArr.sort((a,b) => a - b).filter((v,i,arr) => arr.indexOf(v) == i).filter((v,i,arr)=>v && v.length < a.length)

    return [begin]

}

q = maximumProductOfParts(1234) // 144
q
q = maximumProductOfParts(4321) // 252
q
q = maximumProductOfParts(4224) // 352
q