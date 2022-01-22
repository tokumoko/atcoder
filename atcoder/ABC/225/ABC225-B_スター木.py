N=int(input())
tyouten=[0]*N
for _ in range(N-1):
    a,b=map(int,input().split())
    tyouten[a-1]+=1
    tyouten[b-1]+=1
print("Yes" if max(tyouten)==N-1 else "No")