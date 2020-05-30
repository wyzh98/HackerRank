#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    cnt_apples, cnt_oranges = 0, 0
    for i in range(len(apples)):
        loc_apple = a + apples[i]
        if s <= loc_apple <= t:
            cnt_apples += 1
    for j in range(len(oranges)):
        loc_orange = b + oranges[j]
        if s <= loc_orange <= t:
            cnt_oranges += 1
    print(cnt_apples)
    print(cnt_oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
