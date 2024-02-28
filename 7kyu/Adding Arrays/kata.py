# def arr_adder(arr):
#     words = []

#     for j in range(len(arr[0])):
#         word = ""
#         for i in range(len(arr)):
#             word += arr[i][j]
#         words.append(word.strip())

#     return " ".join(words)


def arr_adder(arr):
    return " ".join(map("".join, zip(*arr)))
