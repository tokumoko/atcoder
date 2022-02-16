N,M=map(int,input().split())
point=[0]*M
ans=0
for i in range(M):
    l,r=map(int,input().split())
    point[i]=(l,r)
    for j in range(i):
        a,b=point[j]
        if ((l<a or l>b) and (a<r<b)) or ((a<l<b) and (r<a or r>b)):
            ans+=1
print(ans)