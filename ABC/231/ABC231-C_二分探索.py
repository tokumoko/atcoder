import bisect
N,Q=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
for i in range(Q):
    x=int(input())
    print(len(A)-bisect.bisect_left(A,x))