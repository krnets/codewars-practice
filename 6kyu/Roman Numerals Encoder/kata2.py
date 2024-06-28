def solution(n):
    to_roman = { 1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M", }
    ans = ""
    for k, v in reversed(to_roman.items()):
        q, n = divmod(n, k)
        for _ in range(q):
            ans += v
    return ans
