#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the migratoryBirds function below.
'''
# This function runs overtime.
def migratoryBirds(arr):
    cnt_max = 0
    for i in range(1, len(arr)):
        cnt = arr.count(i)
        if cnt > cnt_max:
            cnt_max = cnt
            idx = i
    return idx
'''

def migratoryBirds(arr):
    d = Counter(arr)
    idx = max(d, key=d.get) # It can return ONE OF the result.
    value_max = d[idx]
    for i, v in d.items():
        if v == value_max and i < idx:
            idx = i
    return idx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
