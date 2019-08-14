def swap(arr,i,j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    return arr
def bubble_sort(arr, foutput):
    if n < 2:
        foutput.write('No more swaps needed.\n')
        #return ['No more swaps needed.\n']
        return
    left = 0
    strs = []
    while left < len(arr) :
        minim = arr[left]
        min_index = left
        right = left + 1
        while right < len(arr):
            if arr[right] < minim:
                minim = arr[right]
                min_index = right
            right += 1
        if left != min_index:
            swap(arr,left, min_index)
            #strs.append('Swap elements at indices {0:} and {1:}.\n'.format(left+1,min_index+1))
            foutput.write('Swap elements at indices {0:} and {1:}.\n'.format(left+1,min_index+1))
        left += 1
    #strs.append('No more swaps needed.\n')
    foutput.write('No more swaps needed.\n')
    return strs
if __name__ == '__main__':
    with open('input.txt','r') as finput:
        n = int(finput.readline())
        arr = list(map(int, finput.readline().rstrip().split()))
    #n = int(input())
    #arr = list(map(int, input().rstrip().split()))
    
    #for x,y in zip(arr, sorted(arr)):
    #    assert x == y
    with open('output.txt','w') as fouput:
        #strs = bubble_sort(arr)
        bubble_sort(arr, fouput)
        #for line in strs:
        #    fouput.write(line)
        for x in arr[:-1]:
            fouput.write('{:} '.format(x))
        fouput.write('{:}'.format(arr[-1]))

