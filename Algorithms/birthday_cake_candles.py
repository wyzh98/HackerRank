#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar_count, ar):
'''
In previous version, it times out in large-scale tests because I did not store the max(ar) before the loop,
but at each loop, which is 'if ar[i] == max(ar)', and it is time consuming.
'''
    cnt = 0
    maxar = max(ar)
    for i in range(ar_count):
        if ar[i] == maxar:
            cnt += 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar_count, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
