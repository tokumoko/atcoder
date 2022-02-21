def find(x):
    if p[x]==-1 : return x
    else :find(p[x])
    return p[x]
def unite(x,y):
    x=find(x)
    y=find(y)
    if x==1:p[y]=
    p[x]=y
    return

n,q=int(input())
x=list(map(int,input().split()))
p=[-1]*n
for i in range(n-1):
    a,b=map(int,input().split())
    a-=1
    b-=1