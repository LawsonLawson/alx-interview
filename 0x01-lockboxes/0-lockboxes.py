#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1,
and each box may contain keys to the other boxes.

Function:
- canUnlockAll(boxes): Determines if all boxes can be opened.

More info:
- boxes is a list of lists
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- There can be keys that do not have boxes
- The first box boxes[0] is unlocked
- Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    This function checks whether all the boxes in the list of lists 'boxes'
    can be unlocked starting from the first box (index 0). Each box may contain
    keys that can unlock other boxes. The function uses a list to track
    collected keys and iterates over the boxes to unlock them.

    Parameters:
    boxes (list of list of int): A list of boxes, where each box is represented
    as a list of keys (integers) that can unlock other boxes.

    Returns:
    bool: True if all boxes can be opened, otherwise False.

    Example Usage:
    --------------
    >>> canUnlockAll([[1], [2], [3], [4], []])
    True

    >>> canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]])
    True

    >>> canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
    False

    Notes:
    ------
    - The function assumes that all keys are positive integers.
    - The first box (index 0) is initially unlocked.
    - The function uses a list to keep track of the keys collected.
    """
    # List to store the keys collected to open boxes, starts with the key to
    # the first box
    keys_collected = [0]
    for current_key in keys_collected:
        for key_in_box in boxes[current_key]:
            if key_in_box not in keys_collected and key_in_box < len(boxes):
                keys_collected.append(key_in_box)
    return len(keys_collected) == len(boxes)
