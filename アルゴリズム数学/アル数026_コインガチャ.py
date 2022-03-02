N=int(input())
ans=0
for i in range(N,0,-1):
    ans+=N/i
print(ans)