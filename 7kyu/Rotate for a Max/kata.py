def max_rot(n):
    digits = str(n)
    ans = n

    for i in range(0, len(digits)-1):
        digits = digits[:i] + digits[i+1:] + digits[i]
        ans = max(ans, int(digits))

    return ans

q = max_rot(38458215)
q
#     85821534

q = max_rot(195881031)
q
#     988103115

q = max_rot(896219342)
q
#     962193428

q = max_rot(69418307)
q
#     94183076
