import math
N,L,W=map(int,input().split())
a=list(map(int,input().split()))+[L+1]
ans=0
k=0
for i in a:
    count=max(0,i-k-1)
    k=i+W
    ans+=math.ceil(count/W)
print(ans)