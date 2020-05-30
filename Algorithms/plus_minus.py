#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(n, arr):
    cntPos, cntNeg = 0, 0
    for i in range(n):
        if arr[i] > 0:
            cntPos += 1
        elif arr[i] < 0:
            cntNeg += 1
    cntZero = n - cntPos - cntNeg
    cntPos, cntNeg, cntZero = map(lambda x:print(x/n), (cntPos, cntNeg, cntZero))
    # or simply print(cntPos/n) ...

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(n, arr)
