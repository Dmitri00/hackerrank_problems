def insert_sort(arr):
    if n < 2:
        return arr
    sorted_arr = [arr[0]]
    for x in arr[1:]:
        insert_pos = 0
        while x <= sorted_arr[insert_pos]:
            insert_pos += 1
        print(insert_pos)
        sorted_arr.insert(insert_pos, x)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    sorted_arr = insert_sort(arr)
    for x,y in zip(sorted_arr, sorted(arr)):
        assert x == y
    print(sorted_arr)

