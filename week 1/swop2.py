def swap(arr,i,j):
    #print(arr,i,j)
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    
    return arr
def bubble_sort(arr):
    if n < 2:
        return ['No more swaps needed.\n']
    left = 0
    strs = []
    #i = 0
    last_swap = 0
    is_sorted = False
    step = +1
    #print(len(arr))
    while not is_sorted:
        left = last_swap
        is_sorted = True
        while left < len(arr) - 1 :
            #print('assert left+1={} < {}'.format(left + 1,len(arr)))
            #assert left + 1 < len(arr)
            if arr[left] > arr[left+1]:
                is_sorted = False
                #print(left+1)
                swap(arr,left, left+1)
                strs.append('Swap elements at indices {0:} and {1:}.\n'.format(left+1,left+2))
                last_swap = left
            left += 1
        right = last_swap
        is_sorted = True
        while right >= 1:
            if arr[right-1] > arr[right]:
                is_sorted = False
                swap(arr,right-1, right)
                strs.append('Swap elements at indices {0:} and {1:}.\n'.format(right,right+1))
                last_swap = right
            right -= 1
    strs.append('No more swaps needed.\n')
    return strs
if __name__ == '__main__':
    with open('input.txt','r') as finput:
        n = int(finput.readline())
        arr = list(map(int, finput.readline().rstrip().split()))
    #n = int(input())
    #arr = list(map(int, input().rstrip().split()))
    strs = bubble_sort(arr)
    #for x,y in zip(arr, sorted(arr)):
    #    assert x == y
    with open('output.txt','w') as fouput:
        for line in strs:
            fouput.write(line)
        for x in arr[:-1]:
            fouput.write('{:} '.format(x))
        fouput.write('{:}'.format(arr[-1]))

