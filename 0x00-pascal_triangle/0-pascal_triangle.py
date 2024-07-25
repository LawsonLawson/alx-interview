#!/usr/bin/env python3

def generate_row(previous_row):
    '''
    Generate the next row in Pascal's triangle given the previous row.

    Args:
        previous_row (List[int]): The previous row of Pascal's triangle.

    Returns:
        List[int]: The next row in Pascal's triangle.
    '''
    # We assume the first element is always 1.
    row = [1]

    # Compute the intermediate values.
    for i in range(1, len(previous_row)):
        row.append(previous_row[i - 1] + previous_row[i])

    # We assume the last element is always [1].
    row.append(1)

    return row


def pascal_triangle(n):
    '''
    Generate Pascal's triangle of size n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        List[List[int]]: A list of lists representing the triangle.
    '''
    if n <= 0:
        return []

    # We assume the first always [1].
    triangle = [[1]]

    for i in range(1, n):
        # Generate the next row using the last row in the triangle.
        next_row = generate_row(triangle[-1])
        triangle.append(next_row)

    return triangle
