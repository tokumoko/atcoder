import sys
sys.setrecursionlimit(10**7)

N,M=map(int,input().split())
p=[-1]*N

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

l=[0]*N
for i in range(M):
    a,b=map(int,input().split())
    a-=1
    b-=1
    if find(a)==find(b):
        print('No')
        exit()
    l[a]+=1
    l[b]+=1
    unite(a,b)
if max(l)<=2:print('Yes')
else: print('No')