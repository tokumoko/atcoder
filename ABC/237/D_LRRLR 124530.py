N=int(input())
S=list(input())
A=[-1]*(N+1)
l=0
r=N
for i in range(N):
    if S[i]=='L':
        A[r]=i
        r-=1
    else:
        A[l]=i
        l+=1
A[l]=N
print(*A)