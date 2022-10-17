# -*- coding: utf-8 -*-  
""" 
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
"""

coordinates = "a1"

if (ord(coordinates[0]) - 96 - int(coordinates[1])) % 2 == 0:
    print(False)
else: print(True)
