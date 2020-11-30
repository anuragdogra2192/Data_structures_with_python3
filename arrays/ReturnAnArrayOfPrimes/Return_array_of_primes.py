"""
Write a program that takes an integer argument and 
returns all the primes between 1 and that integer.

For example, if the input is 18, you should return [2, 3, 5, 7, 11, 13, 17]

Hint: Exclude the multiples of primes.
"""
#Given n, return all primes up to and including n.

def generate_primes(n):
    primes = []
    # is_prime[p] represents if p is prime or not.
    # Initially, set each to 'true', expecting 0 and 1. Then use sieving to eliminate nonprimes.
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if is_prime[p]:
            primes.append(p)
            # Sieve p's multiples.
            for i in range(p * 2, n + 1, p):
                is_prime[i] = False
    return primes

print("Input the integer: ")
n = int(input())

print("The array of primes: ", generate_primes(n))

#O(nloglogn)