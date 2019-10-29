// 7kyu - Simple Fun 74 - Growing Plant

function growingPlant(upSpeed, downSpeed, desiredHeight) {
    let days = 1
    for (let i = upSpeed; i < desiredHeight; i += (upSpeed - downSpeed))
        days++
    return days
}

q = growingPlant(100, 10, 910) // 10
q
q = growingPlant(10, 9, 4) // 1
q