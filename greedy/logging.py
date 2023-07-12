# boj_2805

N,M=map(int,input().split())
tree=list(map(int,input().split()))

tree.sort()
start,end=0,max(tree)

while start <= end:
    mid=(start+end)//2
    res=sum([i-mid if i>mid else 0 for i in tree])
    if res>=M:
        start=mid+1
    else:
        end=mid-1
print(end)