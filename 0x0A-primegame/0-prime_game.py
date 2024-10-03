#!/usr/bin/python3
"""
Program that performs a prime number game between two players: Maria and Ben
"""


def isWinner(rounds, nums):
    """
    Determines the winner of a prime number game.

    Parameters:
    rounds (int): The number of rounds.
    nums (list): List of numbers representing the upper limits of each round.

    Returns:
    str: The name of the winner ("Maria" or "Ben") or None if it's a tie.
    """

    # Edge case: no numbers provided or less than 1 round
    if not nums or rounds < 1:
        return None

    # Find the maximum number in nums to create the sieve up to this value
    max_num = max(nums)

    # Create a boolean sieve to mark prime numbers
    prime_sieve = [True for _ in range(max(max_num + 1, 2))]

    # Use the Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not prime_sieve[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            prime_sieve[j] = False

    # Mark 0 and 1 as non-prime numbers
    prime_sieve[0] = prime_sieve[1] = False

    # Precompute the number of primes up to each index
    prime_count = 0
    for i in range(len(prime_sieve)):
        if prime_sieve[i]:
            prime_count += 1
        prime_sieve[i] = prime_count

    # Initialize Maria's win count
    maria_wins = 0

    # For each round, determine if Maria wins (odd number of primes)
    for num in nums:
        # If the number of primes up to 'num' is odd, Maria wins the round
        maria_wins += prime_sieve[num] % 2 == 1

    # If the number of rounds Maria won is exactly half of the total
    # rounds, it's a tie
    if maria_wins * 2 == len(nums):
        return None

    # If Maria won more than half the rounds, she wins
    if maria_wins * 2 > len(nums):
        return "Maria"

    # Otherwise, Ben wins
    return "Ben"
