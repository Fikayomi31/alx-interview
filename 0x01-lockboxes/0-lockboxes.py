#!/usr/bin/python3
"""lockbox"""


def canUnlockAll(boxes):
    """method that determines if all boxes can be opened
    Arg:
        boxes -- a list of lists
    Return: True if all boxes can be opened else false
    """
    total_box = len(boxes)  # total number of tge boxes
    setofkey = [0]  # to give track of the array in the total_box
    counter = 0  # use to loop the setofkey
    index = 0  # looping through the boxes

    # looping throught the total_key
    while index < len(setofkey):
        # getting the value in the first box
        set_key = setofkey[index]
        print(set_key)
        for key in boxes[set_key]:
            # appending to value if not in setofkey
            if 0 < key < total_box and key not in setofkey:
                setofkey.append(key)
                counter += 1
        index += 1
    return counter == total_box - 1
