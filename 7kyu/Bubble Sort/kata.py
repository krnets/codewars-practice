def bubble(lst):
    res = []
    swapped = False

    # for i in range(len(lst) - 1):
    #     for j in range(0, len(lst) - i - 1):
    #         if lst[j] > lst[j + 1]:
    #             lst[j], lst[j + 1] = lst[j + 1], lst[j]
    #             swapped = True
    #             res.append(lst[:])
    #     if not swapped:
    #         break

    for n in range(len(lst) - 1, 0, -1):
        for i in range(n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
                res.append(lst[:])
        if not swapped:
            break

    return res
