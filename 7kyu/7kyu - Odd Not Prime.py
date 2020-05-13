# 7kyu - Odd Not Prime

""" For "x", determine how many positive integers less than or equal to "x" are odd but not prime. 
Assume "x" is an integer between 1 and 10000.

Example: 5 has three odd numbers (1,3,5) and only the number 1 is not prime, so the answer is 1
Example: 10 has five odd numbers (1,3,5,7,9) and only 1 and 9 are not prime, so the answer is 2 """


# def is_prime(n):
#     return n > 1 and all(n % i for i in range(3, int(n**0.5)+1), 2)

# def odd_not_prime(n):
#     return len([i for i in range(1, n+1, 2) if not is_prime(i)])

def not_prime(n):
    if n == 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return True
    return False

# def not_prime(n):
#     return any(n % i == 0 for i in range(3, int(n**0.5)+1, 2))

def odd_not_prime(n):
    return 1 + sum(not_prime(i) for i in range(1, n+1, 2))


q = odd_not_prime(5), 1
q
q = odd_not_prime(10), 2
q
q = odd_not_prime(99), 26
q
q = odd_not_prime(233), 67
q
