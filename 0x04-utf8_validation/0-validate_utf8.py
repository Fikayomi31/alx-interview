#!/usr/bin/python3
""" Method that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    # Help to give track of many byte
    count = 0
    for byte in data:
        # check if byte is within ASCI value
        if not 0 <= byte <= 255:
            return False
        # we will start reading the byte
        if count == 0:
            # this check if byte is == 0 and shift
            # all the bit of the byte to right by 7 position by 0
            if byte >> 7 == 0b0:
                continue

            # check if byte is start from 0b110 which is 2 byt
            # and shift bit of the byte to right by 5 position
            elif byte >> 5 == 0b110:
                count = 1
            # check if byte start from 0b1110 which is 3 byte
            # and shift bit of the byte to right by 4 position
            elif byte >> 4 == 0b1110:
                count = 2
            # check if byte start from 0b11110 which is 4 byte
            # and shift bit of the byte to right by 5 position
            elif byte >> 3 == 0b11110:
                count = 3
            else:
                return False
        else:
            # check if byte is a continuation byte
            if byte >> 6 == 0b10:
                count -= 1
            else:
                return False
    return count == 0
