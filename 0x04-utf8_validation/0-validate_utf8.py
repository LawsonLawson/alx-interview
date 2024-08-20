#!/usr/bin/python3

"""
UTF-8 Validation

This module contains a function that checks whether a given list of integers
represents a valid UTF-8 encoded sequence.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): A list of integers where each integer represents a
        byte (8 bits).

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """

    # Initialize the number of bytes expected in the current UTF-8 character
    remaining_bytes_to_process = 0

    # Masks to identify the most significant bits of a byte
    first_bit_mask = 1 << 7  # 10000000 in binary
    second_bit_mask = 1 << 6  # 01000000 in binary

    # Loop over each integer in the data list
    for byte in data:
        # Mask to extract the first bit of the current byte
        first_bit_check_mask = 1 << 7  # Reset for each byte

        # If no more bytes are expected for the current character
        if remaining_bytes_to_process == 0:
            # Count how many leading 1's are in the first byte
            # (determining the number of bytes in the UTF-8 character)
            while first_bit_check_mask & byte:
                remaining_bytes_to_process += 1
                first_bit_check_mask = first_bit_check_mask >> 1

            # If the byte is a single byte UTF-8 character (0xxxxxxx), move
            # to the next byte
            if remaining_bytes_to_process == 0:
                continue

            # UTF-8 characters can only be between 2 and 4 bytes long
            if remaining_bytes_to_process == 1 or \
                    remaining_bytes_to_process > 4:
                return False  # Invalid UTF-8 sequence

        else:
            # Check if the byte is a valid continuation byte (10xxxxxx)
            if not (byte & first_bit_mask and not (byte & second_bit_mask)):
                return False  # Invalid UTF-8 sequence

        # Decrement the number of bytes expected for the current UTF-8
        remaining_bytes_to_process -= 1

    # If there are no remaining bytes expected, the UTF-8 sequence is valid
    return remaining_bytes_to_process == 0
