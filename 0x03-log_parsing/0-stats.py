#!/usr/bin/python3

import sys


def print_statistics(status_code_counts, total_file_size):
    """
    Prints the accumulated statistics, including the total file size and the
    count of each status code.

    Args:
        status_code_counts (dict): A dictionary containing the counts of
        various HTTP status codes. total_file_size (int): The sum of the
        file sizes from all processed log lines.

    Returns:
        None
    """
    print("File size: {}".format(total_file_size))
    for status_code, count in sorted(status_code_counts.items()):
        if count != 0:
            print("{}: {}".format(status_code, count))

# Initialize variables to keep track of total file size, current status code
# and line counter


total_file_size = 0
status_code = 0
line_counter = 0

# Dictionary to store counts of each status code
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        # Split the line into components and reverse it for easier access
        # to file size and status code
        parsed_line = line.split()[::-1]

        if len(parsed_line) > 2:
            line_counter += 1

            # Accumulate the total file size and increment the relevant status
            # code count
            total_file_size += int(parsed_line[0])
            status_code = parsed_line[1]

            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

            # Print statistics after every 10 lines
            if line_counter == 10:
                print_statistics(status_code_counts, total_file_size)
                line_counter = 0

finally:
    # Ensure final statistics are printed upon completion or interruption
    print_statistics(status_code_counts, total_file_size)
