def wordify(n):
    up_to_20 = [ "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", 
                "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty" ]
    tens = [ "", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
    res = []

    if n > 99:
        m, n = divmod(n, 100)
        res.append(up_to_20[m])
        res.append("hundred")
    if n > 20:
        m, n = divmod(n, 10)
        res.append(tens[m])
    if n > 0:
        res.append(up_to_20[n])

    return " ".join(res)
