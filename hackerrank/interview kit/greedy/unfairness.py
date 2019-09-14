#!/bin/python3
# https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    sorted_arr = sorted(arr)
    min_unfairness = sorted_arr[k-1] - sorted_arr[0]
    for i in range(k,len(arr)):
        max_subarr = sorted_arr[i]
        min_subarr = sorted_arr[i-k+1]
        unfairness = max_subarr - min_subarr
        if unfairness < min_unfairness:
            min_unfairness = unfairness
    return min_unfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
