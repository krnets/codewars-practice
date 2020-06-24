""" 7kyu - Reverser

Impliment the reverse function, which takes in input n and reverses it. 
For instance, reverse(123) should return 321. 
You should do this without converting the inputted number into a string.

Fundamentals | Recursion | Algorithms | Computability Theory | Theoretical Computer Science | Functions | Control Flow """


# def reverse(n):
#     rev = 0
#     while n:
#         rev = rev * 10 + n % 10
#         n = n // 10
#     return rev

def reverse(n, rev=0):
    if n == 0:
        return rev
    return reverse(n // 10, rev * 10 + n % 10)

# def reverse(n, rev=0):
#     return reverse(n // 10, rev * 10 + n % 10) if n else rev

q = reverse(1234), 4321
q
q = reverse(10987), 78901
q
q = reverse(1020), 201
q
