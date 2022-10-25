# -*- coding: utf-8 -*-  
""" 
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
"""

import numpy as np

mat = [[1, 2], [3, 4]]
r = 2
c = 4

x, y = np.array(mat).shape
np.reshape(mat, (min(r, x), min(c, y)))
