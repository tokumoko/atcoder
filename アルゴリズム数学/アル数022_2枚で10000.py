n=int(input())
a=list(map(int,input().split()))
b=[0]*100000
ans=0
for i in range(n):
    ans+=b[a[i]]
    b[100000-a[i]]+=1
print(ans)