#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    GAP = 3
    grades_round = []
    for i in range(len(grades)):
        if grades[i] <= 40-GAP:
            grades_round.append(grades[i])
        else:
            mod = grades[i] % 5        # examine the mod of 5
            if mod >= GAP:
                grades_round.append(grades[i] - mod + 5)
            else:
                grades_round.append(grades[i])
    return grades_round

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
