// 8kyu - Define a card suit

/* You get any card as an argument. Your task is to return a suit of this card.
Our deck (is preloaded)

('3♣') -> return 'clubs'
('3♦') -> return 'diamonds'
('3♥') -> return 'hearts'
('3♠') -> return 'spades' */

let deck = ['2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
    '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
    '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',
    '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠'
];

// function defineSuit(card) {
//     let suits = ['clubs', 'diamonds', 'hearts', 'spades']
//     return suits[Math.floor(deck.indexOf(card) / 13)]
// }

function defineSuit(card) {
    return ['clubs', 'diamonds', 'hearts', 'spades'][~~(deck.indexOf(card) / 13)]
}

q = defineSuit('3♣') // 'clubs'
q
q = defineSuit('Q♠') // 'spades'
q
q = defineSuit('9♦') // 'diamonds'
q
q = defineSuit('J♥') // 'hearts'
q
q = defineSuit('A♠')
q
q = defineSuit('2♦')
q
q = defineSuit('2♥')
q
q = defineSuit('2♠')
q