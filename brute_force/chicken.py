# boj_16439

from itertools import combinations
import sys

N, M = map(int, input().split())

priority_list = []
for i in range(N):
    priority_list.append(list(map(int, input().split())))

comb = list(combinations(range(M), 3))

total_score_list = []
for i, j, k in comb:
    total_score = 0
    for l in range(N):
        total_score += max(priority_list[l][i], priority_list[l][j], priority_list[l][k])
    total_score_list.append(total_score)

print(max(total_score_list))