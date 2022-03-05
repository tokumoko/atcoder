import math
s=list(input())
q=int(input())
n=len(s)
for _ in range(q):
    t,k=map(int,input().split())
    l=max(math.ceil(math.log(k,2)),1)
    left=0
    right=2**l