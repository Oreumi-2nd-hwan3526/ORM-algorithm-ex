# boj_11047

N,K=map(int,input().split())
coin=[]

for i in range(N):
    coin.append(int(input()))

coin.reverse()

res=0
for val in coin:
    res+=K//val
    K%=val

print(res)