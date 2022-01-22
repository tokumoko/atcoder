import bisect
N=int(input())
A=list(map(int,input().split()))
Q=int(input())
A.sort()
for i in range(Q):
    B=int(input())
    ind=bisect.bisect_right(A,B)
    if ind==N:print(B-A[ind-1])
    else:print(min(abs(A[ind-1]-B),abs(A[ind]-B)))