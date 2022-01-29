N,S=map(int,input().split())
N=min(S-1,N)
ans=0
for i in range(1,N+1):
    ans+=min(S-i,N)
print(ans)