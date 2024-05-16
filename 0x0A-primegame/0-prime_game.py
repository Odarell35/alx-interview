#!/usr/bin/python3
"""
PrimeGame Module
"""

def isWinner(x, nums):
    """
    Determine the winner of a series of rounds of a game between Maria and Ben.

    Args:
        x (int): Number of rounds to be played.
        nums (list of int): Array of integers representing the ending values for each round.

    Returns:
        str or None: Name of the player that won the most rounds. Returns 'Maria' or 'Ben'
        if there's a clear winner. Returns None if the winner cannot be determined.

    Raises:
        None
    """

    def isPrime(limit):
        """
        Generate prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.

        Args:
            limit (int): Upper limit for generating prime numbers.

        Returns:
            list of int: List of prime numbers up to the specified limit.

        Raises:
            None
        """
        primes = []
        sieve = [True] * (limit + 1)
        for num in range(2, limit + 1):
            if sieve[num]:
                primes.append(num)
                for multiple in range(num * num, limit + 1, num):
                    sieve[multiple] = False
        return primes

    def can_win(n):
        """
        Determine if Maria can win for a given value of 'n'.

        Args:
            n (int): Ending value for a round of the game.

        Returns:
            bool: True if Maria can win, False otherwise.

        Raises:
            None
        """
        primes = isPrime(n)
        return len(primes) % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
