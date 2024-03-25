#!/usr/bin/python3
"""This file attempts to check if a string is a valid UTF8 encoding
"""


def validUTF8(data):
    """Checks if the numbers in the data is a valid utf8 encoding

    Args:
        data (int): a sequence representing bytes
    """
    num_bytes_to_process = 0

    for byte in data:
        # Check if it's a continuation byte (starts with 10)
        if byte & 0xC0 == 0x80:
            if num_bytes_to_process == 0:
                return False
            num_bytes_to_process -= 1
        else:
            # Count the number of bytes to process based on the first byte
            if num_bytes_to_process > 0:
                return False
            if byte & 0x80 == 0:
                num_bytes_to_process = 0
            # check whether it 2 bytes which is 0xC0 is 110
            # and 0xE0 is also 1110
            elif byte & 0xE0 == 0xC0:
                num_bytes_to_process = 1
            # check whether it 3 byte which 0xF0 is 11110
            elif byte & 0xF0 == 0xE0:
                num_bytes_to_process = 2
            # check whether it 4 byte which 0xF8 is 111110
            elif byte & 0xF8 == 0xF0:
                num_bytes_to_process = 3
            else:
                return False

    return num_bytes_to_process == 0
