# boj_11399

N=int(input())
time=list(map(int,input().split()))

time.sort()
res=0
for n in range(N):
    res+=time[n]*(N-n)

print(res)