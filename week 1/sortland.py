def sortland(salaries):
    salaries_sorted = sorted(salaries)
    min_index = -1
    max_index = -1
    med_index = -1
    minim = salaries_sorted[0]
    maxim = salaries_sorted[-1]
    mid = len(salaries)//2
    median = salaries_sorted[mid]
    count = 3
    for i, x in enumerate(salaries):
        if x == minim:
            min_index = i
            count -= 1
        if x == maxim:
            max_index = i
            count -= 1
        if x == median:
            med_index = i
            count -= 1
        if count == 0:
            break
    return min_index, med_index, max_index

if __name__ == '__main__':
    n = int(input())
    arr = list(map(float, input().rstrip().split()))
    min_index, med_index, max_index = sortland(arr)
    print(min_index, med_index, max_index)