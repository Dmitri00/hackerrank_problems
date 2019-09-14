#!/bin/python3
# https://www.hackerrank.com/challenges/making-candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
import math
import os
import random
import re
import sys

# Complete the minimumPasses function below.
def balanced_buy(m,w,cost)
def time_required(m,w,goal,current,m_buy=0,w_buy=0,cost=0):
    candies_required = goal - current + (m_buy+w_buy)*cost
    current_speed = (m+m_buy)*(w+w_buy)
    return math.ceil(candies_required/current_speed)
def minimumPasses(m, w, p, n):

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    mwpn = input().split()

    m = int(mwpn[0])

    w = int(mwpn[1])

    p = int(mwpn[2])

    n = int(mwpn[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
