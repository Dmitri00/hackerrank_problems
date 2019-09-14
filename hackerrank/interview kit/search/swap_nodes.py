#!/bin/python3
# https://www.hackerrank.com/challenges/swap-nodes-algo/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
import os
import sys

#
# Complete the swapNodes function below.
#

from collections import deque
# assume that root node has index 01
def tree_symmetric_traverse(tree_array):
    root_node_index = 0
    node = root_node_index
    null_node = -1
    left = lambda node: tree_array[node][0]
    right = lambda node: tree_array[node][1]
    
    node_stack = deque()
    node_stack.append(-1)
    nodes = []
    #print(node_stack)
    while True:
        #print(node)
        if node != null_node:
            node_stack.append(node)
            #print(node_stack)
            node = left(node)
        else:
            node = node_stack.pop()
            #print(node_stack)
            if node == null_node:
                break
            else:
                nodes.append(node)
                #print(node_stack)
                node = right(node)
    return nodes
            
def build_tree(indexes):
    tree_array = [[0,0,0] for i in range(len(indexes))]
    tree_array[0][2] = 1
    for i, node in enumerate(indexes):
        left = node[0]
        right = node[1]
        if left != -1:
            left -= 1
        if right != -1:
            right -= 1
        tree_array[i][0] = left
        tree_array[i][1] = right
        curr_height = tree_array[i][2]
        if left != -1:
            tree_array[left][2] = curr_height + 1
        if right != -1:
            tree_array[right][2] = curr_height + 1
    return tree_array

def swapNodes(indexes, queries):
    #
    # Write your code here.
    #

    tree_array = build_tree(indexes)
    #print(tree_array)
    results = []
    for query_k in queries:
        for i in range(len(tree_array)):
            node = tree_array[i]
            node_height = node[2]
            if node_height % query_k == 0:
                temp = tree_array[i][0]
                tree_array[i][0] = tree_array[i][1]
                tree_array[i][1] = temp
        
        traverse = tree_symmetric_traverse(tree_array)
        for i in range(len(traverse)):
            traverse[i] += 1
        #result = ' '.join(traverse)
        #print(result)
        results.append(traverse)
    return results

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
    #fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    #fptr.write('\n')

    #fptr.close()
