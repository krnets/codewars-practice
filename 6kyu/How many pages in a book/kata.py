# def amount_of_pages(summary):
#     s, count = "", 0
#     for i in range(1, summary + 1):
#         count += 1
#         s += str(i)
#         if len(s) >= summary:
#             break
#     return count



# def amount_of_pages(summary):
#     num_digits = 0
#     for i in range(1, summary):
#         num_digits += len(str(i))
#         if num_digits == summary:
#             return i
#     return summary



def amount_of_pages(summary):
    n = 0
    while summary > 0:
        n += 1
        if   1     <= n <= 9:     summary -= 1
        elif 10    <= n <= 99:    summary -= 2
        elif 100   <= n <= 999:   summary -= 3
        elif 1000  <= n <= 9999:  summary -= 4
        elif 10000 <= n <= 99999: summary -= 5
    return n