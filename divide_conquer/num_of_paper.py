# boj_1780

import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                for k in range(0, 3):
                    for l in range(0, 3):
                        solution(x+N//3 * k, y+N//3 * l, N//3)
                return
            
    if color == -1:
        result.append(-1)
    elif color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0, 0, N)

print(result.count(-1))
print(result.count(0))
print(result.count(1))