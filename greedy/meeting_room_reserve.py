# boj_1931

import sys

N=int(input())
meeting=[]
for i in range(N):
    start,end=map(int,sys.stdin.readline().split())
    meeting.append([start,end])

meeting.sort(key=lambda x:(x[1],x[0]))

res=0
end_time=0

for i in range(N):
    if meeting[i][0] >=end_time:
        res+=1
        end_time=meeting[i][1]

print(res)