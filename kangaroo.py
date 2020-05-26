#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
'''
An interesting question.
Main idea is to classify t = (x2-x1)/(v1-v2)
'''
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return 'YES'
        else:
            return 'NO'
    else:
        t = (x2 - x1) / (v1 - v2)
        if t > 0 and t % 1 == 0:
            return 'YES'
        else:
            return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
