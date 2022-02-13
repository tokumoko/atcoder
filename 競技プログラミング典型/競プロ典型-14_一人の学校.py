N=int(input())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())))
ans=0
for i in range(N):
    ans+=abs(A[i]-B[i])
print(ans)