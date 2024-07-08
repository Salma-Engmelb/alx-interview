#!/usr/bin/python3
"""
This module contains a function that determines if all boxes can be unlocked.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    
    Args:
        boxes (list of lists): A list of lists, where each sublist contains keys to other boxes.
        
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    opened = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in opened and key < n:
                opened.add(key)
                stack.append(key)
    
    return len(opened) == n
