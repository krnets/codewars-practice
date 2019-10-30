// 7kyu - Move Zeros

function move_zeros(arrNum, isRight = true) {

    let zeros  = arrNum.filter(v => v === 0)
    let nozero = arrNum.filter(v => v !== 0)

    return isRight ? [...nozero, ...zeros] : 
                     [...zeros, ...nozero]
}


q = move_zeros([12, 0, 10, 0, 8, 12, 7, 6, 0, 4, 10, 12, 0], true) // [12, 10, 8, 12, 7, 6, 4, 10, 12, 0, 0, 0, 0]
q
q = move_zeros([12, 0, 10, 0, 8, 12, 7, 6, 0, 4, 10, 12, 0], false) // [0, 0, 0, 0, 12, 10, 8, 12, 7, 6, 4, 10, 12]
q
q = move_zeros([12, 0, 10, 0, 8, 12, 7, 6, 0, 4, 10, 12, 0]) // [12, 10, 8, 12, 7, 6, 4, 10, 12, 0, 0, 0, 0]
q