#!/bin/python3
# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
import math
import os
import random
import re
import sys
from bisect import bisect_left

def find_left(arr, value):
    pos = bisect_left(arr, value)
    if pos != len(arr) and arr[pos] == value:
        return pos
    else:
        return -1

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    sorted_cost_args = sorted(zip(cost,range(len(cost))), key=lambda x: x[0])
    cost_permutation = [0 for i in range(len(cost))]
    sorted_cost = [0 for i in range(len(cost))]

    for i,(flavor_cost, index) in enumerate(sorted_cost_args):
        sorted_cost[i] = flavor_cost
        cost_permutation[i] = index
    
    max_pos = bisect_left(sorted_cost, money)
    if max_pos == 0:
        #print('Too few money')
        return
    elif max_pos == len(sorted_cost):
        max_pos = max_pos - 1
    max_cost = sorted_cost[max_pos]
    min_pos = bisect_left(sorted_cost, money - max_cost)
    if min_pos >= len(sorted_cost) - 1:
        #print('Too much money')
        return
    min_cost = sorted_cost[min_pos]

    sorted_cost = sorted_cost[min_pos:max_pos+1]
    cost_permutation = cost_permutation[min_pos:max_pos+1]
    #print(sorted_cost, cost_permutation)
    for i in range(len(sorted_cost) - 1):
        cost_ = sorted_cost[i]
        search_cost = money - cost_
        possible_pos = find_left(sorted_cost[i+1:], search_cost)
        if possible_pos != -1:
            possible_pos += 1 + i
            #print('search for',cost_,search_cost)
            #print(possible_pos)
            assert search_cost == sorted_cost[possible_pos]
            #print('found',cost_,sorted_cost[possible_pos])
            real_index1 = cost_permutation[i] + 1
            real_index2 = cost_permutation[possible_pos] + 1
            #print(real_index1, real_index2)
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
