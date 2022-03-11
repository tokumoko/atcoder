#強連結成分分解
import sys
sys.setrecursionlimit(10000)
def dfs(w):
    t[w]=False
    for j in g[w]:
        if t[j]:dfs(j)
    label.append(w)
    return
def ndfs(w,count):
    t[w]=False
    for j in ng[w]:
        if t[j]:count=ndfs(j,count+1)
    return count

n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
ng=[[] for _ in range(n+1)]
label=[]
for i in range(m):
    a,b=map(int,input().split())
    g[a].append(b)
    ng[b].append(a)
t=[True]*(n+1)
for i in range(1,n+1):
    if t[i]:dfs(i)
t=[True]*(n+1)
ans=0
label.reverse()
for i in label:
    if t[i]:
        a=ndfs(i,1)
        ans+=a*(a-1)//2
print(ans)