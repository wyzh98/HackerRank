#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(n, arr):
    # Write your code here
    priDiagonal, secDiagonal = 0, 0
    for i in range(n):
        priDiagonal += arr[i][i]      # the index of primary diagonal is a_ii
    for j in range(n):
        secDiagonal += arr[j][n-j-1]  # the index of secondary diagonal is a_i(n-j-1)
    return abs(priDiagonal - secDiagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
