#!/usr/bin/python3
"""lockboxes file for implementations to possible keys to locks"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened"""
    n = len(boxes)
    unlocked = set()
    to_check = [0]

    while to_check:
        box = to_check.pop()
        if box not in unlocked:
            unlocked.add(box)
            for key in boxes[box]:
                if key < n and key not in unlocked:
                    to_check.append(key)

    return len(unlocked) == n
