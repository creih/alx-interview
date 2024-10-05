#!/usr/bin/python3
"""
This module defines and implements a prime number guessing algorithm for determining the winner.
"""

def isWinner(x, nums):
    """ Determines the winner of the prime number guessing game between Maria and Ben """
    if x <= 0 or any(n < 1 for n in nums):
        return None
    def sieve_of_eratosthenes(n):
        """ Returns a list of prime numbers up to n """
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n + 1, i):
                    sieve[j] = False
        return sieve
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            prime_count = sum(primes[2:n+1])
            if prime_count % 2 != 0:
                maria_wins += 1
            else:
                ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
