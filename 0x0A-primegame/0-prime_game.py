#!/usr/bin/env python3
""""
this module defines and implements a prime number guesing algorithm for winner
"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """
        Return a list of primes up to n using the sieve of Eratosthenes
        """
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return [i for i in range(n + 1) if sieve[i]]
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    def play_round(n):
        """ Simulates a round of the game """
        remaining = set(range(1, n + 1))
        current_player = 0
        while True:
            prime = next((p for p in primes if p in remaining), None)
            if not prime:
                return current_player ^ 1
            to_remove = {prime * i for i in range(1, n // prime + 1)}
            remaining.difference_update(to_remove)
            current_player ^= 1

    maria_wins, ben_wins = 0, 0
    for n in nums:
        winner = play_round(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
