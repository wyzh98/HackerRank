#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    cnt_min, cnt_max = 0, 0
    score_min, score_max = scores[0], scores[0]
    for i in range(1, len(scores)):
        if scores[i] < score_min:
            score_min = scores[i]
            cnt_min += 1
        elif scores[i] > score_max:
            score_max = scores[i]
            cnt_max += 1
    return cnt_max, cnt_min


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
