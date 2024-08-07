#!/usr/bin/python3

"""
Module: min_operations

This module contains a function to calculate the minimum number of operations
needed to achieve exactly `n` 'H' characters in a text file using copy and
paste operations.

Functions:
    - min_operations(target_chars: int) -> int: Calculates the minimum
    number of operations needed to achieve exactly `target_chars` 'H'
    characters.
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations needed to achieve exactly
    `target_chars` 'H' characters using copy and paste operations.

    Parameters:
    target_chars (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations needed, or 0 if `target_chars` is
    less than 2.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
            divisor -= 1
        divisor += 1

    return operations
