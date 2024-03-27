# def diagonal(matrix):
#     principal_sum, secondary_sum = 0, 0
#     n = len(matrix)

#     for i in range(n):
#         principal_sum += matrix[i][i]
#         secondary_sum += matrix[i][n - i - 1]

#     return ("Principal Diagonal win!"
#         if principal_sum > secondary_sum
#         else "Secondary Diagonal win!" if secondary_sum > principal_sum else "Draw!")


def diagonal(matrix):
    balance = sum(matrix[i][i] - matrix[i][-i - 1] for i in range(len(matrix)))

    return ("Draw!" 
            if balance == 0 
            else f"{('Principal', 'Secondary')[balance < 0]} Diagonal win!")
