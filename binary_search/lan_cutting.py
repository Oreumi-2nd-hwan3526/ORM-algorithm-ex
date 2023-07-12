# boj_1654

import sys

K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1, max(lan)

while start<=end:
    
    mid = (start + end) // 2

    total_count = 0

    for i in lan:
        total_count += (i // mid)

    if total_count >= N:
        start = mid + 1
    
    elif total_count < N:
        end = mid - 1

print(end)
