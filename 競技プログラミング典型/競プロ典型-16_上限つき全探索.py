N=int(input())
A,B,C=map(int,input().split())
L=min(10000,N//min(A,B,C)+1)
ans=10000
for i in range(L):
    for j in range(L-i):
        score=N-(A*i+B*j)
        k=score//C
        if A*i+B*j+C*k==N and score>=0:
            ans=min(ans,i+j+k)
print(ans)