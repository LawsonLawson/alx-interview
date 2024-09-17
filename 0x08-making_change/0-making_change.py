#!/usr/bin/python3

"""
Contains the makeChange function for calculating the fewest coins needed to
meet a target total.
"""


def makeChange(coinDenominations, targetTotal):
    """
    Determines the fewest number of coins needed to meet a given total using
    the provided denominations.

    Args:
        coinDenominations (list): A list of available coin denominations
        (positive integers).
        targetTotal (int): The target total value to reach using the fewest
        coins.

    Returns:
        int: The fewest number of coins needed to meet the targetTotal.
             - If the targetTotal is 0 or less, returns 0 (no coins are needed)
             - If the targetTotal cannot be met using any combination of the
             available coins, returns -1.

    Example:
        makeChange([1, 5, 10], 12) -> 3 (10 + 1 + 1)
    """
    # If no coins are provided or the list is None, return -1 (invalid input)
    if not coinDenominations or coinDenominations is None:
        return -1

    # If the total is 0 or less, no coins are needed
    if targetTotal <= 0:
        return 0

    # Initialize the number of coins needed
    fewestCoins = 0

    # Sort the coin denominations in descending order
    coinDenominations = sorted(coinDenominations, reverse=True)

    # Iterate over each coin denomination
    for coin in coinDenominations:
        # Use as many of the current coin as possible
        while coin <= targetTotal:
            targetTotal -= coin
            fewestCoins += 1

        # If the total is reached, return the fewest number of coins used
        if targetTotal == 0:
            return fewestCoins

    # If the loop ends and the total is not 0, return -1 (cannot meet total)
    return -1
