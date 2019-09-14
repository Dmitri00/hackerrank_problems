#!/bin/python3
# https://www.hackerrank.com/challenges/minimum-time-required/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
import math
import os
import random
import re
import sys
from functools import reduce
from decimal import Decimal
from collections import deque
from bisect import bisect_left

# Complete the minTime function below.
def minTime(machines, goal):
    events_queue = deque()
    Time = 0
    total = 0
    velocity_total = Decimal(0)
    
    goal_dec = Decimal(goal)
    speed = reduce(lambda x,y: x+ Decimal(1/y), machines, Decimal(0))
    estimated_time = int(math.floor(goal_dec/speed))
    Time = estimated_time
    total = 0
    for machine_id,machine_time in enumerate(machines):
        candies_made = int(math.floor(Time/machine_time))
        total += candies_made
        next_time = (candies_made+1)*machine_time
        next_event = (next_time, machine_id)
        insert_pos = bisect_left(events_queue,next_event)
        events_queue.insert(insert_pos, next_event)
    while total < goal:
        Time = events_queue[0][0]
        while len(events_queue) > 0 and events_queue[0][0] == Time:
            event = events_queue.popleft()
            machine_id = event[1]
            total += 1
            next_time = Time + machines[machine_id]
            next_event = (next_time, machine_id)
            insert_pos = bisect_left(events_queue,next_event)
            events_queue.insert(insert_pos, next_event)
    return Time


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
