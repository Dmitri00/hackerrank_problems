#!/bin/python3
# https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
import math
import os
import random
import re
import sys
from bisect import bisect_right
def unique_gen(arr):
    prev_elem = None
    for elem in arr:
        if elem != prev_elem:
            yield elem
        prev_elem = elem
# Complete the triplets function below.
def triplets(a, b, c):
    a,b,c = list(map(sorted, (a,b,c)))
    a,b,c = list(map( lambda x: list(unique_gen(x)), (a,b,c) ))
    num_triplets = 0
    prev_q = None
    for q in b:
        if q == prev_q:
            continue
        n1 = bisect_right(a,q)
        n2 = bisect_right(c,q)
        num_triplets += n1*n2
        prev_q = q
    return num_triplets


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
