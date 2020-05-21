# 8kyu - Define a card suit

""" You get any card as an argument. Your task is to return a suit of this card.

Our DECK (is preloaded)

('3C') -> return 'clubs'
('3D') -> return 'diamonds'
('3H') -> return 'hearts'
('3S') -> return 'spades' """

DECK = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS',
        '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
        '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
        '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC']


def define_suit(card):
    return ['spades', 'diamonds', 'hearts', 'clubs'][DECK.index(card) // 13]


q = define_suit('2S')  # 'spades'
q
q = define_suit('AS')  # 'spades'
q

q = define_suit('2D')  # 'diamonds'
q
q = define_suit('AD')  # 'diamonds'
q

q = define_suit('2H')  # 'hearts'
q
q = define_suit('AH')  # 'hearts'
q

q = define_suit('2C')  # 'clubs'
q
q = define_suit('AC')  # 'clubs'
q

q = define_suit('QS')  # 'spades'
q
q = define_suit('9D')  # 'diamonds'
q
q = define_suit('JH')  # 'hearts'
q
