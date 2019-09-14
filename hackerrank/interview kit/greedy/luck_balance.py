#!/bin/python3

# https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
import math
import os
import random
import re
import sys
from functools import reduce

# Complete the luckBalance function below.
def luckBalance(k, contests):
    unimportant = list(filter(lambda x:x[1] == 0, contests))
    unimportant_sum = reduce(lambda x,y:x+y[0],unimportant, 0)
    #print(unimportant)
    important = list(filter(lambda x:x[1] == 1, contests))
    important = sorted(important, key=lambda x:x[0])
    #print(important)
    num_lost_important = min(k, len(important))
    num_won_important = len(important) - num_lost_important
    if num_lost_important == 0:
        important_lost = 0
        important_won = reduce(lambda x,y:x+y[0],important, 0)
    elif num_won_important == 0:
        important_lost  = reduce(lambda x,y:x+y[0],important, 0)
        important_won = 0
    else:
        important_lost = reduce(lambda x,y:x+y[0],important[-num_lost_important:], 0)
        important_won = reduce(lambda x,y:x+y[0],important[:num_won_important], 0)
    return unimportant_sum+important_lost-important_won

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)
    print(result)
    #fptr.write(str(result) + '\n')

    #fptr.close()
