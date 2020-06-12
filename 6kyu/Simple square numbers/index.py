""" 6kyu - Simple square numbers

In this Kata, you will be given a number n (n > 0) 
and your task will be to return the smallest square number N (N > 0) 
such that n + N is also a perfect square. 
If there is no answer, return -1.

solve(13) = 36
# because 36 is the smallest perfect square that can be added to 13 to form a perfect square => 13 + 36 = 49

solve(3) = 1 # 3 + 1 = 4, a perfect square
solve(12) = 4 # 12 + 4 = 16, a perfect square
solve(9) = 16 
solve(4) = -1 """

# kata forfeited, solution unlocked - previous attemps all timed out after 12 sec

def solve(n):
    for i in range(int(n**0.5), 0, -1):
        x = n - i**2
        if x > 0 and x % (2*i) == 0:
            return ((n - i ** 2) // (2 * i)) ** 2
    return -1


q = solve(290101), 429235524
q
q = solve(1), -1
q
q = solve(2), -1
q
q = solve(3), 1
q
q = solve(4), -1
q
q = solve(5), 4
q
q = solve(7), 9
q
q = solve(8), 1
q
q = solve(9), 16
q
q = solve(10), -1
q
q = solve(11), 25
q
q = solve(13), 36
q
q = solve(17), 64
q
q = solve(88901), 5428900
q
