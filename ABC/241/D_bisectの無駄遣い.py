from bisect import bisect_left,bisect_right,insort
q=int(input())
a=[]
for _ in range(q):
    query=list(map(int,input().split()))
    if query[0]==1:
        insort(a,query[1])
    elif query[0]==2:
        n=bisect_right(a,query[1])
        if n>=query[2]:print(a[n-query[2]])
        else:print(-1)
    else:
        n=bisect_left(a,query[1])
        if len(a)-n>=query[2]:print(a[n+query[2]-1])
        else:print(-1)