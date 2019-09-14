#!/bin/python3

# https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

import math
import os
import random
import re
import sys
from copy import copy

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    flowers = sorted(c, reverse=True)
    price_coeff = [1 for i in range(k)]
    friend_i = 0
    total_price = 0
    for flower in flowers:
        total_price += price_coeff[friend_i]*flower
        price_coeff[friend_i] += 1
        friend_i = (friend_i + 1) % k
        
    
    return total_price


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
