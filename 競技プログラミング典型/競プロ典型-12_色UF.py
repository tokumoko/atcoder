def q1(r,c):
    X[r][c]=1
    if r!=0 and X[r-1][c]!=0:
        unite(r*W+c,(r-1)*W+c)
    if c!=0 and X[r][c-1]!=0:
        unite(r*W+c,r*W+c-1)
    if r!=H-1:
        if X[r+1][c]!=0:
            unite(r*W+c,(r+1)*W+c)
    if c!=W-1:
        if X[r][c+1]!=0:
            unite(r*W+c,r*W+c+1)
    return
def find(x):
    if p[x]==-1 : return x
    else :
        p[x]=find(p[x])
        return p[x]
def unite(x,y):
    x=find(x)
    y=find(y)
    if x==y: return
    p[x]=y
    return
def q2(ra,ca,rb,cb):
    if find(ra*W+ca)==find(rb*W+cb) and X[ra][ca]!=0:print('Yes')
    else:print('No')

H,W=map(int,input().split())
X=[[0]*W for _ in range(H)]
p=[-1]*(H*W)
Q=int(input())
for i in range(Q):
    a=list(map(int,input().split()))
    if a[0]==1:
        q1(a[1]-1,a[2]-1)
    else:
        q2(a[1]-1,a[2]-1,a[3]-1,a[4]-1)