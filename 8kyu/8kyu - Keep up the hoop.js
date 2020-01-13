// 8kyu - Keep up the hoop

function hoopCount(n) {
    return n < 10 ? 'Keep at it until you get it' : 'Great, now move on to tricks'
}

q = hoopCount(3) // "Keep at it until you get it" 
q
q = hoopCount(11) // "Great, now move on to tricks"
q