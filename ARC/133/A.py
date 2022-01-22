N=int(input())
A=list(map(int,input().split()))
x=A[N-1]
for i in range(N-1):
    if A[i]>A[i+1]:
        x=A[i]
        break
A=[str(i) for i in A if i!=x]
print(' '.join(A))