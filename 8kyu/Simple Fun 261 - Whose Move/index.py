# 8kyu - Simple Fun #261: Whose Move

""" Two players - "black" and "white" are playing a game. 
The game consists of several rounds. If a player wins in a round, he is to move again during the next round. 
If a player loses a round, it's the other player who moves on the next round. 
Given whose turn it was on the previous round and whether he won, determine whose turn it is on the next round.

[input] string lastPlayer/$last_player
"black" or "white" - whose move it was during the previous round.

[input] boolean win/$win
true if the player who made a move during the previous round won, false otherwise.

[output] a string
Return "white" if white is to move on the next round, and "black" otherwise.

For lastPlayer = "black" and win = false, the output should be "white".
For lastPlayer = "white" and win = true, the output should be "white". """

# def whoseMove(lastPlayer, win):
#     if lastPlayer == 'black' and win == False:
#         return 'white'
#     if lastPlayer == 'white' and win == True:
#         return 'white'
#     if lastPlayer == 'black' and win == True:
#         return 'black'
#     if lastPlayer == 'white' and win == False:
#         return 'black'

# def whoseMove(lastPlayer, win):
#     return lastPlayer if win else 'white' if lastPlayer == 'black' else 'black'

# def whoseMove(lastPlayer, win):
#     return ['black', 'white'][(lastPlayer == 'black') ^ win]

def whoseMove(lastPlayer, win):
    return lastPlayer if win else {'white': 'black', 'black': 'white'}.get(lastPlayer)


q = whoseMove('black', False)  # 'white'
q
q = whoseMove('white', False)  # 'black'
q
q = whoseMove('black', True)  # 'black'
q
q = whoseMove('white', True)  # 'white'
q
