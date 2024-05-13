#!/usr/bin/python3
"""Prime Game Module """
def isWinner(x, nums):
    """ function that announces winner"""
    def isPrime(num):
        """Finds Prime number"""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    def calculateWinner(n):
        """calculates winner"""
        primes = [num for num in range(2, n + 1) if isPrime(num)]
        primes_set = set(primes)
        total_numbers = set(range(2, n + 1))
        maria_turn = True
        while total_numbers:
            if maria_turn:
                for prime in primes:
                    if prime in total_numbers:
                        total_numbers -= set(range(prime, n + 1, prime))
                        maria_turn = False
                        break
            else:
                for num in total_numbers:
                    if num not in primes_set:
                        total_numbers.remove(num)
                        maria_turn = True
                        break
        return "Maria" if maria_turn else "Ben"

    winners = {"Maria": 0, "Ben": 0}
    for n in nums:
        winner = calculateWinner(n)
        winners[winner] += 1

    max_wins = max(winners.values())
    if list(winners.values()).count(max_wins) == 1:
        return max(winners, key=winners.get)
    else:
        return None


