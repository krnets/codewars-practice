# 8kyu - Rock Paper Scissors!

""" Let's play! You have to return which player won! In case of a draw return Draw!.

Examples:

rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw! """


# def rps(p1, p2):
#     if ((p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock')):
#         return 'Player 1 won!'
#     elif ((p1 == 'scissors' and p2 == 'rock') or (p1 == 'paper' and p2 == 'scissors') or (p1 == 'rock' and p2 == 'paper')):
#         return 'Player 2 won!'
#     else:
#         return 'Draw!'

def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return 'Player 1 won!'
    elif beats[p2] == p1:
        return 'Player 2 won!'
    else:
        return 'Draw!'


# Test.it('player 1 win')
q = rps('rock', 'scissors')  # "Player 1 won!"
q
q = rps('scissors', 'paper')  # "Player 1 won!"
q
q = rps('paper', 'rock')  # "Player 1 won!"
q

# Test.it('player 2 win')
q = rps('scissors', 'rock')  # "Player 2 won!"
q
q = rps('paper', 'scissors')  # "Player 2 won!"
q
q = rps('rock', 'paper')  # "Player 2 won!"
q

# Test.it('draw')
q = rps('rock', 'rock')  # 'Draw!'
q
q = rps('scissors', 'scissors')  # 'Draw!'
q
q = rps('paper', 'paper')  # 'Draw!'
q
