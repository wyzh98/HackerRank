#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hr = int(s[:2])
    mi = int(s[3:5])
    sec = int(s[6:8])
    
    # charactorize
    # 0,1,...,11AM 0,1,...,11
    # 12        PM 12
    # 1,2,...,11PM 13,14,...,23
    # 12        AM 00
    if hr == 12:
        hr = '00' if s[8:]=='AM' else '12'  # special when hr=12
    else:
        hr = str(hr).zfill(2) if s[8:]=='AM' else str(hr+12).zfill(2)  # zfill() is to format, e.g. 2 -> 02
    mi = str(mi).zfill(2)
    sec = str(sec).zfill(2)
    return hr + ':' + mi + ':' + sec

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
