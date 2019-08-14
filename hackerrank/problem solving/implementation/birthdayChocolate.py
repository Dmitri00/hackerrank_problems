#!/bin/python3
#https://www.hackerrank.com/challenges/the-birthday-bar/problem
import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    if len(s) < m:
        return 0
    sum_ = 0
    for i in range(m):
        sum_ += s[i]
    count = 0
    if sum_ == d:
        count += 1
    first_i = 0
    for i in range(m,len(s)):
        sum_ = sum_ - s[first_i] + s[i]
        first_i += 1
        if sum_ == d:
            count += 1
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()

