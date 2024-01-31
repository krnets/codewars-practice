def longest_consec(strarr, k):
    if not strarr or k > len(strarr) or k <= 0:
        return ""
    ans = ""
    for i in range(len(strarr) - k + 1):
        consec = "".join(strarr[i : i + k])
        if len(consec) > len(ans):
            ans = consec
    return ans
