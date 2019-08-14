#!/bin/python3
#https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    if n < 2:
        return 1
    substCount = 0
    prev = None
    count_seq = 0
    for i, char in enumerate(s):
        count_seq += 1
        if i and char != prev:
            j = 1
            while  (i - j >= 0) and  (i + j < n) and  j <= count_seq:
                if s[i-j] == prev == s[i+j]:
                    j += 1
                    substCount += 1
                else:
                    break
            count_seq = 1
        substCount += count_seq
        prev = char
    return substCount


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
