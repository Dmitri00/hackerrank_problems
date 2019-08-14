def swap(arr,i,j):
    #print(arr,i,j)
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    
    return arr
def bubble_sort(arr):
    if n < 2:
        return arr,['No more swaps needed.\n']
    N = len(arr)
    strs = []
    
    sorted_indexes = sorted(zip(arr, range(N)), key = lambda x:x[0])
    
    #arr = sorted_indexes[:][0]
    substitute = sorted_indexes
    #print(arr)
    #print(substitute)
    index_set = set(list(range(len(arr))))
    while len(index_set) > 0:
        first = index_set.pop()
        #index_set.add(first)
        #index_set.remove(first)
        curr_ind = first
        next_ind = substitute[first][1]
        #print(first,next_ind)
        if curr_ind == next_ind:
            continue
        while next_ind != first:
            #print(curr_ind,next_ind,first)
            if curr_ind  < next_ind:
                left = curr_ind + 1
                right = next_ind + 1
            else:
                left = next_ind + 1
                right = curr_ind + 1
            strs.append('Swap elements at indices {0:} and {1:}.\n'.format(left,right))
            index_set.remove(next_ind)
            curr_ind = next_ind
            next_ind = substitute[curr_ind][1]            
    strs.append('No more swaps needed.\n')
    return sorted(arr), strs
if __name__ == '__main__':
    with open('input.txt','r') as finput:
        n = int(finput.readline())
        arr = list(map(int, finput.readline().rstrip().split()))
    #n = int(input())
    #arr = list(map(int, input().rstrip().split()))
    sorted_arr, strs = bubble_sort(arr)
    #print(arr)
    #for x,y in zip(arr, sorted(arr)):
    #    assert x == y
    with open('output.txt','w') as fouput:
        for line in strs:
            fouput.write(line)
        for x in sorted_arr[:-1]:
            fouput.write('{:} '.format(x))
        fouput.write('{:}'.format(sorted_arr[-1]))

