# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    char_counter = Counter()
    freq_counter = Counter()
    for char in s:
        old_freq = char_counter[char]
        if old_freq != 0:
            freq_counter[old_freq] -= 1
        new_freq = old_freq + 1
        char_counter[char] = new_freq
        freq_counter[new_freq] += 1
    frequensies = list(filter(lambda kv: kv[1] != 0, freq_counter.items()))
    print(frequensies)
    answer = 'NO'
    if len(frequensies) == 1:
        answer = 'YES'
    elif len(frequensies) == 2:
        freq1 = frequensies[0][0]
        freq2 = frequensies[1][0]
        count_freq1 = frequensies[0][1]
        count_freq2 = frequensies[1][1]
        if freq1 == 1 and count_freq1 == 1:
            answer = 'YES'
        elif freq1 == 1 and count_freq1 == 1:
            answer = 'YES'
        elif freq2 - freq1 == 1 and count_freq2 == 1:
            answer = 'YES'
        elif freq1 - freq2 == 1 and count_freq1 == 1
            answer = 'YES'
    return answer

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)
    print(result)
    #fptr.write(result + '\n')

    #fptr.close()
