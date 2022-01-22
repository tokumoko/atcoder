n,x=map(int,input().split())
a=list(map(int,input().split()))
s=[0 for _ in range(n)]
n=0
while s[x-1]==0:
    s[x-1]=1
    n+=1
    x=a[x-1]
print(n)