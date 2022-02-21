n,x=map(int,input().split())
l=[False]*(x+1)
l[0]=True
for i in range(n):
    a,b=map(int,input().split())
    for j in range(x,-1,-1):
        if l[j]:
            if j+a<=x:l[j+a]=True
            if j+b<=x:l[j+b]=True
            l[j]=False
print('Yes' if l[x]!=0 else 'No')