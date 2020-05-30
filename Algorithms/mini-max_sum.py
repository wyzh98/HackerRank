#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    minSum = sum(arr) - arr[-1] # min sum of a sorted array is the sum of first four numbers
    maxSum = sum(arr) - arr[0]
    print(minSum, maxSum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
