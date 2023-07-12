# boj_1920

N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))


def binary_search(start, end, target, array):

    while start<=end:
        
        mid = (start + end) // 2

        if array[mid] == target:
            return 1
        
        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1
        
    return 0

A.sort()

for num in arr:
    print(binary_search(0, len(A)-1, num, A))