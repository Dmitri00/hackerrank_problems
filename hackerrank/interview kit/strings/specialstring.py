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
    substCount = 1
    cake = s[0]
    nach = None

    new_cake = None
    new_cake_i = n-1

    is_nach = False
    left_n = 1
    right_n = 0

    i = 1

    binomial_n_2 = lambda n: n*(n+1)/2
    while i < n + 1:
        #char = s[i]
        print(i)
        if i < n and s[i] == cake:
            if not is_nach:
                left_n += 1
                substCount += left_n
            else:
                right_n += 1
                
            i += 1
        else:
            if not is_nach and i < n:
                is_nach = True
                nach = s[i]
                new_cake_i = i
                
                new_cake = s[i]
                i += 1
            else:
                substCount += min(left_n, right_n)
                #print('substCount=',substCount)
                is_nach = False
                cake = new_cake
                new_cake = None
                i = new_cake_i + 1
                #print('i=',i)
                left_n = 1
                right_n = 0
                if cake != None:
                    substCount += left_n
                if i == n:
                    break
    return substCount


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
