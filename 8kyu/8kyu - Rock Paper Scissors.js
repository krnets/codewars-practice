// 8kyu - Rock Paper Scissors!

// const rps = (p1, p2) => p1 == 'rock' && p2 == 'scissors' ||
//                         p1 == 'scissors' && p2 == 'paper' || 
//                         p1 == 'paper' && p2 == 'rock' ? 'Player 1 won!' : 
//                         p1 == 'scissors' && p2 == 'rock' || 
//                         p1 == 'paper' && p2 == 'scissors' ||
//                         p1 == 'rock' && p2 == 'paper' ? 'Player 2 won!' :
//                         'Draw!'

const rps = (p1, p2) => {
    if (p1 == p2) return 'Draw!'
    let rules = { rock: 'scissors', paper: 'rock', scissors: 'paper' }
    if (p2 == rules[p1]) return 'Player 1 won!'
    else return 'Player 2 won!'
}

// Player 1 won!
q = rps('rock', 'scissors')
q
q = rps('scissors', 'paper')
q
q = rps('paper', 'rock')
q

// Player 2 won!
q = rps('scissors', 'rock')
q
q = rps('paper', 'scissors')
q
q = rps('rock', 'paper')
q

// 'Draw!'
q = rps('rock', 'rock'), 'Draw!'
q
q = rps('scissors', 'scissors'), 'Draw!'
q
q = rps('paper', 'paper'), 'Draw!'
q