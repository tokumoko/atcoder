import sys
sys.setrecursionlimit(2*10**5)
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
n, m = map(int, input().split())
p = [-1] * (n)
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    unite(a,b)
val = find(0)
ans = True
for i in range(1,n):
    if val != find(i):
        ans = False
if ans:
    print('The graph is connected.')
else:
    print('The graph is not connected.')