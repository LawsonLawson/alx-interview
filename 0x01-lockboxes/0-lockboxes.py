#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked.

You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1, and each box may contain keys to the other boxes.

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
    Determines if all the boxes can be opened.

    This function checks whether all the boxes in the list of lists 'boxes'
    can be unlocked starting from the first box (index 0). Each box may contain
    keys that can unlock other boxes. The function uses a set to track
    collected keys and iterates over the boxes to unlock them.

    Parameters:
    boxes (list of list of int): A list of boxes, where each box is represented
    as a list of keys(integers) that can unlock other boxes.

    Returns:
    bool: True if all boxes can be opened, otherwise False.

    Example Usage:
    --------------
    >>> canUnlockAll([[1], [2], [3], [4], []])
    True

    >>> canUnlockAll([[1, 4], [2], [3], [], [0]])
    True

    >>> canUnlockAll([[1, 2, 3], [], [], [], []])
    False

    Notes:
    ------
    - The function assumes that all keys are positive integers.
    - The first box (index 0) is initially unlocked.
    - The function uses a set to keep track of the keys collected.
    """
    number_of_boxes = len(boxes)
    # Set of keys we have (start with the key to the first box)
    keys = {0}
    # List to track which boxes have been unlocked
    unlocked = [False] * number_of_boxes
    # The first box is initially unlocked
    unlocked[0] = True

    def unlock(box_index):
        """
        Recursively unlock boxes.

        Parameters:
        box_index (int): The index of the current box to unlock.
        """
        for key in boxes[box_index]:
            if key < number_of_boxes and not unlocked[key]:
                unlocked[key] = True
                keys.add(key)
                unlock(key)

    unlock(0)

    return all(unlocked)
