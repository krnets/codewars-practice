# 6kyu - Pure odd digits primes

""" Primes that have only odd digits are pure odd digits primes, obvious but necessary definition. 
Examples of pure odd digit primes are: 11, 13, 17, 19, 31... 

If a prime has only one even digit does not belong to pure odd digits prime, 
no matter the amount of odd digits that may have.

Create a function, only_oddDigPrimes(), that receive any positive integer n, and output a list like the one bellow:

[number pure odd digit primes bellow n, 
largest pure odd digit prime smaller than n, 
smallest pure odd digit prime higher than n]

Let's see some cases:

only_oddDigPrimes(20) ----> [7, 19, 31]
///7, beacause we have seven pure odd digit primes bellow 20 and are 3, 5, 7, 11, 13, 17, 19
19, because is the nearest prime of this type to 20
31, is the first pure odd digit that we encounter after 20///

only_oddDigPrimes(40) ----> [9, 37, 53]

In the case that n, the given value, is a pure odd prime, should be counted it with the found primes 
and search for the inmediately bellow and the inmediately after. """

# def only_oddDigPrimes (n): # P.O.D.P (pure ood digit prime)
#     # your code goes here
#     return [number of P.O.D.Ps, largest P.O.D.P smaller than n, smaller P.O.D.P bigger than n]

def is_prime(n):
    return n > 1 and all(n % i for i in range(3, int(n**0.5)+1, 2))

def only_odd_digits(n):
    return all(int(x) % 2 for x in str(n))

def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

def only_oddDigPrimes(n):
    res = [i for i in range(n+1) if is_prime(i) and only_odd_digits(i)]
    while True:
        n = next_prime(n)
        if only_odd_digits(n):
            return [len(res), res[-1], n]

# [number pure odd digit primes bellow n,
# largest pure odd digit prime smaller than n,
# smallest pure odd digit prime higher than n]


q = only_oddDigPrimes(20), [7, 19, 31]
q
q = only_oddDigPrimes(40), [9, 37, 53]
q
q = only_oddDigPrimes(55), [10, 53, 59]
q
q = only_oddDigPrimes(60), [11, 59, 71]
q
