# def fill_gaps(timesheet):
#     i, n = 0, len(timesheet)
#     out = timesheet[:]

#     while i < n:
#         j = i + 1

#         while j < n and out[j] is None:
#             j += 1

#         if j < n and out[j] == out[i]:
#             k = i + 1

#             while k < j:
#                 out[k] = out[i]
#                 k += 1

#         if j == i:
#             i += 1
#         else:
#             i = j

#     return out


def fill_gaps(timesheet):
    out = timesheet[:]
    prev = None
    for i, v in enumerate(out):
        if v is not None:
            if v == prev:
                out[gap_start:i] = [v] * (i - gap_start)
            gap_start = i + 1
            prev = v
    return out
