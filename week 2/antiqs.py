def antiqs(n):
    return list(range(n-1,0,-1))
if __name__ == '__main__':
    with open('input.txt','r') as finput:
        n = int(finput.readline())
    #n = int(input())
    #arr = list(map(int, input().rstrip().split()))
    arr = antiqs(n)
    #print(arr)
    #for x,y in zip(arr, sorted(arr)):
    #    assert x == y
    with open('output.txt','w') as fouput:
        for x in arr[:-1]:
            fouput.write('{:} '.format(x))
        fouput.write('{:}'.format(arr[-1]))

